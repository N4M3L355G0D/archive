/*
 *  cputool.h - Headers for the cputool utility
 *  Copyright (C) 2012-2013, AllWorldIT
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

#ifndef _CPUTOOL_H
#define _CPUTOOL_H  1


#include <signal.h>
#include <stdio.h>


//USER_HZ detection, from openssl code
#ifndef HZ
# if defined(_SC_CLK_TCK) \
     && (!defined(OPENSSL_SYS_VMS) || __CTRL_VER >= 70000000)
#  define HZ ((double)sysconf(_SC_CLK_TCK))
# else
#  ifndef CLK_TCK
#   ifndef _BSD_CLK_TCK_ /* FreeBSD hack */
#    define HZ  100.0
#   else /* _BSD_CLK_TCK_ */
#    define HZ ((double)_BSD_CLK_TCK_)
#   endif
#  else /* CLK_TCK */
#   define HZ ((double)CLK_TCK)
#  endif
# endif
#endif


/* Structure to hold the info we get from /proc/X/stat */
struct cputool_stat { 
	int pid; // %d 
    char comm[256]; // %s
    char state; // %c
    int ppid; // %d
    int pgrp; // %d
    int session; // %d
    int tty_nr; // %d
    int tpgid; // %d
    unsigned long flags; // %lu
    unsigned long minflt; // %lu
    unsigned long cminflt; // %lu
    unsigned long majflt; // %lu
    unsigned long cmajflt; // %lu
    unsigned long utime; // %lu
    unsigned long stime; // %lu
    long cutime; // %ld
    long cstime; // %ld
    long priority; // %ld
    long nice; // %ld
    long num_threads; // %ld
    long itrealvalue; // %ld
    unsigned long starttime; // %lu
    unsigned long vsize; // %lu
    long rss; // %ld
    unsigned long rlim; // %lu
    unsigned long startcode; // %lu
    unsigned long endcode; // %lu
    unsigned long startstack; // %lu
    unsigned long kstkesp; // %lu
    unsigned long kstkeip; // %lu
    unsigned long signal; // %lu
    unsigned long blocked; // %lu
    unsigned long sigignore; // %lu
    unsigned long sigcatch;	// %lu
    unsigned long wchan; // %lu
    unsigned long nswap; // %lu
    unsigned long cnswap; // %lu
    int exit_signal; // %d
    int processor; // %d
    unsigned long rt_priority; // %lu 
    unsigned long policy; // %lu 
    unsigned long long delayacct_blkio_ticks; // %llu 
};

/* Format of the /proc/X/stat file */
char const *CPUTOOL_STAT_FORMAT = "%d %s %c %d %d %d %d %d %lu %lu %lu %lu %lu %lu %lu %ld %ld %ld %ld %ld %ld %lu %lu %ld %lu %lu %lu %lu %lu %lu %lu %lu %lu %lu %lu %lu %lu %d %d %lu %lu %llu";


/* List of PID's we're watching */
struct cputool_pidlist_item {
	pid_t pid;
	pid_t pgrp;
	FILE *fd;
	int status;

	struct cputool_pidlist_item *next;
};

/* PID list flags */
#define CPUTOOL_PID_INACTIVE 0
#define CPUTOOL_PID_ACTIVE 1
#define CPUTOOL_PID_FDOPEN 2


#endif

/*vim: ts=4*/
