/*
 *  cputool.c - CPU & load managmenet tool
 *  Copyright (C) 2012-2014, AllWorldIT
 *  Copyright (C) 2012, Nigel Kukard <nkukard@lbsd.net>
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include "config.h"

#include "cputool.h"

#include <dirent.h>
#include <errno.h>
#include <fcntl.h>
#include <getopt.h>
#include <math.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>



/* How accurate is the clock, per second? */
#define CLOCK_PRECISION 1000000
/* How many times do we plan to sleep per second? */
#define DEFAULT_SLEEP CLOCK_PRECISION / 10


/* Be verbose? */
int verbose = 0;

/* These two child variable are used for the signalling function */
pid_t child_pid = 0;
pid_t child_pgid = 0;
/* List of PID's we're currently monitoring */
struct cputool_pidlist_item *gPidList;
int isRunning = 0;

int child_external = 0;
/* Use with the SIGUSR1 and SIGUSR2 to stop/resume suspending/unsuspending */
int canStopProcesses = 1;
/* Continue loopin flag */
int loop = 1;

/* Counters */
uint64_t statsSlowdowns = 0;
uint64_t statsTimeDelayed = 0;



/* Print out our usage */
static void printUsage(char **argv) {
	printf("%s - Copyright (c) 2012-2014, AllWorldIT\n",PACKAGE_STRING);
	printf("Usage: %s [-c PCNT] [-l LOAD] [[-p PID | -P PID] | [--] COMMAND ...]\n",argv[0]);
	printf("\n");
	printf("Options:\n");
	printf("    -p,  --pid <PID>              Manage the CPU usage of a specific PID\n");
	printf("    -P,  --pid-pgrp <PID>         Manage the CPU usage of a specific PID's entire\n");
	printf("                                  process group.\n");
	printf("    -c,  --cpu-limit <PCNT>       Percentage of CPU to limit process to. Integer value.\n");
	printf("    -l,  --load-limit <LOAD>      Load to limit process to. Decimals allowed\n");
/*
	printf("    -f,  --frequency=<FREQ>       Maximum number of times a second to check CPU\n");
	printf("                                  usage. This value is still dynamic, but this\n");
	printf("                                  option defines the maximums. Valid values are\n");
	printf("                                  between 2 - 100.\n");
*/
	printf("    -v,  --verbose                Be verbose, -vv, more verbose, -vvv most verbose.\n");
	printf("    -V,  --version                Show version identifier.\n");
	printf("    -h,  --help                   Display this help page\n");
	printf("\n");
}

static void printHelpHint() {
	fprintf(stderr,"Use --help for available options.\n");
}

static void printPPCHint() {
	fprintf(stderr,"You must specify exactly one of -p, -P or [command].\n");
}

/*
 * PID list functions
 */

/* Create a new item */
static struct cputool_pidlist_item *pidListItemNew(struct cputool_pidlist_item **parent) {
	struct cputool_pidlist_item *item = (struct cputool_pidlist_item *) malloc(sizeof(struct cputool_pidlist_item));


	/* Check for failure */
	if (!item) {
		return NULL;
	}

	/* If we have a parent link it in */
	if (parent) {
		(*parent)->next = item;
	}

	item->next = NULL;

	return item;
}

/* Find last unused item, or create new */
static struct cputool_pidlist_item *pidListItemGet(struct cputool_pidlist_item *pidList) {
	struct cputool_pidlist_item *p, *last = NULL;
	struct cputool_pidlist_item *new = NULL;


	/* Loop and find last unused */
	for (p = pidList; p; p = p->next) {
		/* Yep, we found one! */
		if (!p->pid) {
			new = p;
			break;
		}
		last = p;
	}
	/* If we could not find one to recycle, create one and link to last one we looped with */
	if (!new) {
		new = pidListItemNew(&last);
		new->pid = 0;
		new->pgrp = 0;
	}

	return new;
}


/*
 * Logging functions
 */

/* Log messsage */
static void logmsg(const char* format, ...)
{
	/* Grab time */
	time_t t = time(NULL);
	struct tm tm = *localtime(&t);
	va_list argptr;

	/* Print out some fancy info */
	fprintf(stderr,"%d-%02d-%02d %02d:%02d:%02d - ", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec);

	/* And the rest of the mssage */
	va_start(argptr, format);
	vfprintf(stderr, format, argptr);
	va_end(argptr);
}


/*
 * Load checking functions
 */

/* Function to grab the load average */
static float getload() {
	float loadavgn = -1.00;
	static char buf[1024];
	char *pos;
	int fd;
	ssize_t len;


	if ((fd = open("/proc/loadavg", O_RDONLY)) > 0) {
		len = read(fd, buf, sizeof(buf) - 1);
		close(fd);
		if (len > -1) {
			buf[len] = '\0';
			loadavgn = strtod(buf, &pos);
		} else {
			logmsg("ERROR: getload()failed with '%s'\n",strerror(errno));
		}
	}

	return loadavgn;
}


/*
 * Functions we use to process /proc
 */

/* Grab the stat info for a process */
static inline int getProcessStatFD(FILE *fd, struct cputool_stat *pstat)
{
	int i;


	/* Scan in stat */
	i = fscanf(fd,CPUTOOL_STAT_FORMAT,
		&pstat->pid,pstat->comm,&pstat->state,&pstat->ppid,&pstat->pgrp,
		&pstat->session,&pstat->tty_nr,&pstat->tpgid,
		&pstat->flags,
		&pstat->minflt,&pstat->cminflt,&pstat->majflt,&pstat->cmajflt,
		&pstat->utime,&pstat->stime,&pstat->cutime,&pstat->cstime,
		&pstat->priority, &pstat->nice,
		&pstat->num_threads,
		&pstat->itrealvalue,
		&pstat->starttime,
		&pstat->vsize,&pstat->rss,&pstat->rlim,
		&pstat->startcode,&pstat->endcode,&pstat->startstack,
		&pstat->kstkesp,&pstat->kstkeip,
		&pstat->signal,&pstat->blocked,
		&pstat->sigignore,&pstat->sigcatch,
		&pstat->wchan,
		&pstat->nswap,&pstat->cnswap,
		&pstat->exit_signal,
		&pstat->processor,&pstat->rt_priority,
		&pstat->policy,
		&pstat->delayacct_blkio_ticks
	);

	/* Check result */
	if (i < 42) {
		return -1;
	}

	return 0;
}


/* Grab an entire process list CPU time */
static uint64_t getProcessListCPUTime()
{
	/* Handles & structures */
	struct cputool_pidlist_item *p;
	static struct cputool_stat pstat;
	/* Combined total of CPU time consumed */
	uint64_t cpuTime = 0;


	/* We about to walk everything, remove ACTIVE flag */
	for (p = gPidList; p; p = p->next) {
		/* If we not yet open */
		if ((p->status | CPUTOOL_PID_FDOPEN) != p->status) {
			static char statfile[32];


			/* Create filename */
			sprintf(statfile, "/proc/%d/stat", p->pid);
			/* Open stat file */
			if (!(p->fd = fopen(statfile,"r"))) {
				continue;
			}

			p->status |= CPUTOOL_PID_FDOPEN;
			/* Do not buffer */
			setvbuf(p->fd, (char *) NULL, _IONBF, 0);
		}

		/* If PID is active & FD is open */
		if (p->status & CPUTOOL_PID_ACTIVE) {
			/* Rewind position in file */
			rewind(p->fd);

			/* Grab process stat for this PID */
			if (!getProcessStatFD(p->fd,&pstat)) {
				cpuTime += pstat.utime + pstat.stime;
			}
		}
	}

	return cpuTime;
}


/* Grab process group members */
static uint64_t getUpdateProcessGroupMembersCPUTime(pid_t pgrp)
{
	/* Handles & structures */
	DIR *proc;
	struct dirent *entry = NULL;
	static struct cputool_stat pstat;
	struct cputool_pidlist_item *p;
	/* Combined total of CPU time consumed */
	uint64_t cpuTime = 0;


	/* Open /proc */
	if ((proc = opendir("/proc")) == NULL) {
		logmsg("ERROR: Failed to opendir() on '/proc': %s\n",strerror(errno));
		return -1;
	}

	/* We about to walk everything, remove ACTIVE flag */
	for (p = gPidList; p; p = p->next) {
		p->status &= ~CPUTOOL_PID_ACTIVE;
	}

	/* Loop reading in directory entries */
	while ((entry = readdir(proc))) {
		FILE *fd = NULL;
		pid_t pid;
		int exists = 0;


		/* If its not a PID directory, continue */
		if (strtok(entry->d_name,"0123456789")) {
			continue;
		}

		/* Set PID we working with */
		pid = atoi(entry->d_name);

		/* Loop through PID's, if it matches, we should use this FD */
		for (p = gPidList; p; p = p->next) {
			/* Found it, make it active, and stop for loop */
			if (p->pid == pid) {
				p->status |= CPUTOOL_PID_ACTIVE;
				/* Set FD */
				if (p->status & CPUTOOL_PID_FDOPEN) {
					fd = p->fd;
					/* REWIND IT!!!! */
					rewind(fd);
				}
				/* It exists in the pidList */
				exists = 1;
				break;
			}
		}

		/* If no FD is opened already, open one */
		if (!fd) {
			static char statfile[32];


			/* Create filename */
			sprintf(statfile, "/proc/%d/stat", pid);
			/* Open stat file */
			if (!(fd = fopen(statfile,"r"))) {
//				logmsg("ERROR: Failed to open '%s': %s\n",statfile,strerror(errno));
				continue;
			}
		}

		/* Grab process stat for this PID */
		if (!getProcessStatFD(fd,&pstat)) {
			struct cputool_pidlist_item *q;
			int isChild = 0;


			/* See if we child of some parent */
			for (q = gPidList; q; q = q->next) {
				if (pstat.ppid == q->pid && q->status & CPUTOOL_PID_ACTIVE) {
					isChild = 1;
					break;
				}
			}

			/* If p->status is acitve, we matched above */
			if (exists) {

				/* If we didn't have an FD, but now do, set it */
				if ((p->status | CPUTOOL_PID_FDOPEN) != p->status) {
					p->status |= CPUTOOL_PID_FDOPEN;
					p->fd = fd;
					/* Do not buffer */
					setvbuf(fd, (char *) NULL, _IONBF, 0);
				}

				cpuTime += pstat.utime + pstat.stime;

			/* If its in our group, then add up the CPU time */
			} else if (pstat.pgrp == pgrp) {

				/* Add to PID list */
				p = pidListItemGet(gPidList);
				p->pid = pstat.pid;
				p->pgrp = pstat.pgrp;
				p->fd = fd;
				p->status = CPUTOOL_PID_ACTIVE | CPUTOOL_PID_FDOPEN;

				/* Do not buffer */
				setvbuf(fd, (char *) NULL, _IONBF, 0);

				cpuTime += pstat.utime + pstat.stime;

				if (verbose > 2) {
					logmsg("NEW pgrp child PID/PGID => %lu/%lu\n",pstat.pid,pstat.pgrp);
				}

			/* If this pid is a child, add it */
			} else if (isChild) {

				/* Add to PID list */
				p = pidListItemGet(gPidList);
				p->pid = pstat.pid;
				p->pgrp = pstat.pgrp;
				p->fd = fd;
				p->status = CPUTOOL_PID_ACTIVE | CPUTOOL_PID_FDOPEN;

				/* Do not buffer */
				setvbuf(fd, (char *) NULL, _IONBF, 0);

				cpuTime += pstat.utime + pstat.stime;

				if (verbose > 1) {
					logmsg("NEW ppid child PID/PGID => %lu/%lu\n",pstat.pid,pstat.pgrp);
				}

			/* We end up here if this is PID is not related to us at all */
			} else {
				fclose(fd);
			}
		}
	}
	/* Close off our handle in /proc */
	closedir(proc);

	/* Loop yet again and close/blank anything not active */
	for (p = gPidList; p; p = p->next) {
		/* Check if bit was not set */ 
		if ((p->status | CPUTOOL_PID_ACTIVE) != p->status) {
			/* Close & reset all data */
			if (p->status & CPUTOOL_PID_FDOPEN) {
				fclose(p->fd);
			}
			p->pid = 0;
			p->pgrp = 0;
			p->status = CPUTOOL_PID_INACTIVE;
		}
	}

	return cpuTime;
}


/* Return time difference between two timevals in ms */
static inline uint64_t timediff_us(const struct timespec *tv1, const struct timespec *tv2)
{
	/* Calculate the total time difference by adding up secs + usecs */
	return (tv1->tv_sec - tv2->tv_sec) * 1000000 + (tv1->tv_nsec - tv2->tv_nsec) / 1000;
}

/* Kill a group + children */
static void killpgm(pid_t pgrp, int signum) {
	struct cputool_pidlist_item *p;


	/* Loop and see if we have some odd children */
	for (p = gPidList; p; p = p->next) {
		/* Signal them if we do */
		if (p->pgrp != pgrp && p->status & CPUTOOL_PID_ACTIVE) {
			if (verbose > 3) {
				logmsg("kill(%i,%i)\n",p->pid,signum);
			}
			kill(p->pid,signum);
		}
	}

	/* Signal main group */
	if (verbose > 3) {
		logmsg("killpg(%i,%i)\n",pgrp,signum);
	}
	killpg(pgrp,signum);
}

/* Signal handling */
static void sigusr1() {
	if (verbose > 3) {
		logmsg("sigusr1()\n");
	}
	signal(SIGUSR1, sigusr1);
	canStopProcesses = 0;
	isRunning = 1;
	killpgm(child_pgid,SIGCONT);
}
static void sigusr2() {
	if (verbose > 3) {
		logmsg("sigusr2()\n");
	}
	signal(SIGUSR2, sigusr2);
	canStopProcesses = 1;
}
static void sighup() {
	struct cputool_pidlist_item *p;


	/* Loop and dump our processes */
	for (p = gPidList; p; p = p->next) {
		if (p->status & CPUTOOL_PID_ACTIVE) {
			logmsg("Process %i group %i\n",p->pid,p->pgrp);
		}
	}
}
/* And the handler itself */
static void signal_handler(int signum) {
	if (verbose > 3) {
		logmsg("signal_handler(%i)\n",signum);
	}

	/* Resume so the child can handle the signal */
	if (child_pgid) {
		killpgm(child_pgid,SIGCONT);
	} else if (child_pid) {
		kill(child_pid,SIGCONT);
	}

	isRunning = 1;

	/* Make sure its not an external process */
	if (!child_external) {

		/* Kill it with the signal we got */
		if (child_pgid) {
			killpgm(child_pgid,signum);
		} else if (child_pid) {
			kill(child_pid,signum);
		}

		/* And wait... */
		waitpid(-1, NULL, 0);
	}

	/* We should not continue looping */
	loop = 0;
}



/* Main program */
int main (int argc, char *argv[]) {

	/* If this variable is set, we spawned a child */
	int haveChild = 0;

	/* PID of process we're working on */
	pid_t pid = 0;
	/* Process GROUP */
	pid_t pgid = 0;
	uint32_t pidListLastCheckusAgo = 0;;
	/* Wait status */
	int waitStatus;

	/* Child is running */
	int exceededLoad = 0;
	int exceededCPU = 0;

	/* Sleep timespec */
	struct timespec sleepTime;
	/* Time now and before */
	struct timespec now;
	struct timespec lastUpdate;

	/* CPU usage now and before, plus the limit */
	uint64_t cpuNow = 0;
	uint64_t cpuLast = 0 ;
	uint32_t cpuLimit = 0;
	double cpuLimitMultiplier;
	double cpuPerHZ;
	/* Load limit */
	double loadLimit = 0.00;
	/* bucket holding how many ticks we can consume */
	double tickBucket = 0;
	double tickBucketMax = 0;
	/* Setup default sleep period */
	uint32_t sleep_us = DEFAULT_SLEEP;

	/* Misc */
	int i;

	/* Our long options */
	struct option long_options[] = {
		{"pid",1,0,'p'},
		{"pid-pgrp",1,0,'P'},
		{"cpu-limit",1,0,'c'},
		{"load-limit",1,0,'l'},
		{"verbose",0,0,'v'},
		{"version",0,0,'V'},
		{"help",0,0,'h'},
		{0,0,0,0}
	};


	/* Setup signals */
	signal(SIGUSR1, sigusr1);
	signal(SIGUSR2, sigusr2);
//	signal(SIGCHLD, sigchld);
	signal(SIGINT, signal_handler);
	signal(SIGHUP, sighup);
	signal(SIGQUIT, signal_handler);
	signal(SIGILL, signal_handler);
	signal(SIGKILL, signal_handler);
	signal(SIGABRT, signal_handler);
	signal(SIGTERM, signal_handler);
	signal(SIGPIPE, signal_handler);
	signal(SIGSEGV, signal_handler);

	/* Loop with options */
	while (1) {
		int option_index = 0;
		char c;

		/* Process */
		c = getopt_long(argc,argv,"p:P:c:l:vVh",long_options,&option_index);

		if (c == -1) {
			break;
		}

		/* Check... */
		switch (c) {
			case 'p':
				if (pid != 0) {
					fprintf(stderr,"%s: Multiple pid/pidgroups specified.\n",argv[0]);
					printPPCHint();
					return 1;
				}
				pid = atoi(optarg);
				break;
			case 'P':
				if (pid != 0) {
					fprintf(stderr,"%s: Multiple pid/pidgroups specified.\n",argv[0]);
					printPPCHint();
					return 1;
				}
				pid = atoi(optarg);
				pgid = pid;
				break;
			case 'c':
				cpuLimit = atoi(optarg);
				/* Check the value range for cpuLimit */
				if (cpuLimit < 1) {
					fprintf(stderr,"%s: The value for -c/--cpu-limit must be in above 1\n",argv[0]);
					return 1;
				}
				break;
			case 'l':
				loadLimit = atof(optarg);
				/* Check the value range for loadLimit */
				if (loadLimit < 0.01) {
					fprintf(stderr,"%s: The value for -l/--load-limit must be above 0.00\n",argv[0]);
					return 1;
				}
				break;
			case 'v':
				verbose++;
				break;
			case 'V':
				printf("%s\n",PACKAGE_STRING);
				return 0;
			case 'h':
				printUsage(argv);
				return 0;
			default:
				printHelpHint();
				return 1;
		}
	}

	/* If we don't have a PID we should have a command to run */
	if (!pid && !pgid && optind == argc) {
		fprintf(stderr,"%s: Nothing to manage. You must specify --pid/-p, --pid-pgid/-P or a command.\n",argv[0]);
		printHelpHint();
		return 1;
	}

	/* If we STILL have params left over, its bad */
	if ((pid || pgid) && optind < argc) {
		while (optind < argc)
			fprintf(stderr,"%s: Invalid argument -- %s.\n",argv[0],argv[optind++]);
		printPPCHint();
		printHelpHint();
		return 1;
	}

	/* If we don't have a PID, its more than likely we must commandline it */
	if (!pid) {
		/* Loop with extra args and build our new execve environment */
		for (i = 0; i < (argc - optind); i++) {
			argv[i] = argv[i + optind];
		}
		/* End it of with NULL */
		argv[i] = NULL;

		haveChild = 1;
		pid = fork();
		if (pid < 0) {
			logmsg("ERROR: Failed to fork new process\n");
			return 1;

		/* Parent */
		} else if (pid > 1) {
			pgid = pid;

		/* Child */
		} else {
			pid = getpid();

			/* Reset parent */
			if (setsid () == -1) {
				logmsg("ERROR: Error resetting PGID\n");
			}

			if (verbose) {
//				logmsg("Child process %i PRIO set to 20\n",pid);
			}

			/* FIXME */
//			setpriority (PRIO_PROCESS, pid, 20);
			execvp(argv[0], argv);

			/* We shouldn't really get here */
			logmsg("ERROR: Failed to execute command '%s': %s\n",argv[0],strerror(errno));
			return 1;
		}

	/* Set process group if we were specified on the commandline */
	} else {
		child_external = 1;
		/* Setup the process group properly, we just set it to pid earlier */
		if (pgid) {
			pgid = getpgid(pid);
		}
	}

	/* Setup child parent group for signalling */
	child_pid = pid;
	child_pgid = pgid;
	/* Initialize our PID list */
	gPidList = pidListItemNew(NULL);
	gPidList->pid = pid;
	gPidList->pgrp = pgid;
	gPidList->status = CPUTOOL_PID_ACTIVE;

	/* Last update is right now */
	clock_gettime(CLOCK_MONOTONIC,&lastUpdate);

	/* Some verbosity ... */
	if (verbose > 1) {
		logmsg("Child PID/PGID => %lu/%lu\n",pid,pgid);
		/* Check what additional debug info we're going to display */
		if (cpuLimit) {
			logmsg(" CPU Limit : %u%%\n",cpuLimit);
		}
		if (loadLimit > 0.00) {
			logmsg(" LOAD Limit: %.2f\n",loadLimit);
		}
		logmsg(" Verbosity: %i\n",verbose);
	}

	/* CPU limit multiplier */
	cpuLimitMultiplier = (float) cpuLimit / (float) 100;
	cpuPerHZ = cpuLimitMultiplier * HZ;

	/* Set max tickBucket size & initialize tickBucket to that */
	tickBucket = tickBucketMax = cpuPerHZ;

	/* Set initial counters */
	if (pgid) {
		cpuLast = cpuNow = getUpdateProcessGroupMembersCPUTime(pgid);
	} else {
		cpuLast = cpuNow = getProcessListCPUTime();
	}

	/* Continue process */
	killpgm(pgid,SIGCONT);
	isRunning = 1;

	/* This is the main program loop */
	while (loop) {
		/* Period from last check (ms) */
		uint64_t elapsed_us;
		/* Were we running here? */
		int wasRunning = isRunning;


		/* Check if we have dead children */
		if (haveChild) {
			if (waitpid(pid, &waitStatus, WNOHANG) < 0) {
				if (verbose > 3) {
					logmsg("Dead child\n");
				}
				break;
			}

		/* Check process is still alive */
		} else if (kill(pid,0) == -1 && errno == ESRCH) {
			if (verbose > 3) {
				logmsg("Process not alive\n");
			}
			break;
		}

		/* We need to grab "now" so we can calculate below */
		clock_gettime(CLOCK_MONOTONIC,&now);
		elapsed_us = timediff_us(&now,&lastUpdate);
		/* Statistics */
		if (!wasRunning) {
			statsTimeDelayed += elapsed_us / 1000;
		}


		/* Are we processing load limits? */
		if (loadLimit > 0.00) {
			double load = getload();

			/* Check if our current load is exceeding our limit, stop */
			if (load > loadLimit) {
				exceededLoad = 1;

			/* If we running and we below the threshold, resume */
			} else {
				exceededLoad = 0;
			}

			if (verbose > 1) {
					logmsg("LOAD LIMIT => wasRunning=%i, load %.2f/%.2f\n",wasRunning,load,loadLimit);
			}
		}

		/* Are we processing cpu limits? */
		if (cpuLimit) {
			/* Change in ticks for period */
			uint64_t ticks_delta;
			/* Number of ticks allowed */
			double ticks_allowed;


			/* Grab current CPU time for entire process group */
			if (pgid) {
				/* 1 second */
				if (pidListLastCheckusAgo > 1000000) {
					cpuNow = getUpdateProcessGroupMembersCPUTime(pgid);
					pidListLastCheckusAgo = 0;
				/* Else just update normally */
				} else {
					cpuNow = getProcessListCPUTime();
					pidListLastCheckusAgo += elapsed_us;
				}

			} else {
				cpuNow = getProcessListCPUTime();
			}

			/* Change in ticks for period */
			ticks_delta = cpuNow - cpuLast;
			/* Number of tickes we can eat */
			ticks_allowed = (double) elapsed_us / (double) CLOCK_PRECISION * cpuPerHZ;

			/* Remove ticks we ate and add ones we allowed */
			tickBucket -= ticks_delta;
			tickBucket += ticks_allowed;

			/* Check we did not exceed 1s */
			if (tickBucket > tickBucketMax) {
				tickBucket = tickBucketMax;

			/* Check if we don't have an insane negative value either */
			} else if (tickBucket < - HZ) {
				tickBucket = - HZ;
			}

			/* If we running and our tick bucket is screwed, stop the process */
			if (tickBucket < 0) {
				exceededCPU = 1;
				/* Loop twice as often as we do to refill tick bucket to 0 */
				sleep_us = fabs(tickBucket) / tickBucketMax * (double) CLOCK_PRECISION;

			/* If we not running and we now have some ticks to consume, start the process */
			} else if (tickBucket > 0) {
				exceededCPU = 0;
				/* Set new sleep time */
				sleep_us = (tickBucket / cpuPerHZ) * CLOCK_PRECISION;
			};

			/* Only use this if its a greater value */
			if (sleep_us < DEFAULT_SLEEP) {
					sleep_us = DEFAULT_SLEEP;

			/* If our value is higher than the clock precision we MUST adjust it lower */
			/* or we will get a error returned */
			} else if (sleep_us > CLOCK_PRECISION - DEFAULT_SLEEP) {
				sleep_us = CLOCK_PRECISION - DEFAULT_SLEEP;
			}

			/* Set last values */
			cpuLast = cpuNow;

			/* Print out info if we're running in verbose mode */
			if (verbose > 1) {
				logmsg("CPU LIMIT => wasRunning=%i, tickBucket = %.2f (allowed += %.2f, consumed -= %llu), elapsed us = %llu, \
						sleep_us = %u\n", wasRunning, tickBucket, ticks_allowed, ticks_delta, elapsed_us, sleep_us);
			}
		}

		/* Set last time we were updated */
		clock_gettime(CLOCK_MONOTONIC,&lastUpdate);

		/* If load is high, override the sleep time */
		if (exceededLoad) {
			sleepTime.tv_sec = 5;
		} else {
			sleepTime.tv_sec = 0;
		}

		/* If we running and we should not be, then stop */
		if ((exceededLoad || exceededCPU) && wasRunning) {

			/* Check if we signalling the process group or process */
			if (pgid) {
				killpgm(pgid,SIGSTOP);
				if (verbose > 2) {
					logmsg("KILLPG: SIGSTOP sent to process group %lu (%lu)\n",pgid,pid);
				}
			} else if (pid) {
				kill(pid,SIGSTOP);
				if (verbose > 2) {
					logmsg("KILLPG: SIGSTOP sent to process %lu\n",pid);
				}
			}

			isRunning = 0;

			statsSlowdowns++;

		/* If we not running and should be then continue */
		} else if (!(exceededLoad || exceededCPU) && !wasRunning) {

			/* Check if we signalling the process group or process */
			if (pgid) {
				killpgm(pgid,SIGCONT);
				if (verbose > 2) {
					logmsg("KILLPG: SIGCONT sent to process group %lu (%lu)\n",pgid,pid);
				}
			} else if (pid) {
				kill(pid,SIGCONT);
				if (verbose > 2) {
					logmsg("KILLPG: SIGCONT sent to process %lu\n",pid);
				}
			}

			isRunning = 1;
		}

		/* Sleep here */
		sleepTime.tv_nsec = sleep_us * 1000;
		nanosleep(&sleepTime,NULL);
	}

	if (verbose) {
		logmsg("STATISTICS: Slowdowns = %llu, Total Time Delayed = %.2Lfs\n",statsSlowdowns,
				(long double) statsTimeDelayed / 1000 );
	}

	/* Make sure we SIGCONT the prcess group when we exit, the parent could of died and children still be alive */
	if (pgid) {
		/* Recalculate the children first */
		getUpdateProcessGroupMembersCPUTime(pgid);
		/* Then signal everything */
		killpgm(pgid,SIGCONT);
	}

	return WEXITSTATUS(waitStatus);
}

// vim: ts=4
