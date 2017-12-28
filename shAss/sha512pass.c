#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <crypt.h>
//auto create random string
#include <sodium.h>
#include <time.h>
//cmd args, for later
#include <argp.h>

//this not meant for password storage, but password generation
float randomNum();
unsigned long dataNum();

int check(char *data,char *salt){
	char *d=malloc(strlen(salt)*4);
	sprintf(d,"$6$%s",salt);
	char *hash = crypt(data,d);
	printf("%s\n",hash);
}

int main1(char *data){
	char *stringBuff;
	char *shaRand;
	int acc=0;
	shaRand=malloc(128*3);
	sprintf(shaRand,"$6$%lu",randomNum());
	stringBuff=malloc(strlen(data)*2);	 
	sprintf(stringBuff,"%s",data,sizeof(data));
	char *hash=crypt(stringBuff,shaRand);
	printf("%s\n",hash);
	
}

float randomNum(){
	char string[128];
	uint32_t rInt;

	randombytes_buf(string,128);
	rInt = randombytes_uniform(dataNum());
	return rInt;
}
unsigned long dataNum(){
	time_t raw_time;
	struct tm *timeinfo;

	time(&raw_time);
	timeinfo=localtime(&raw_time);
	char *num;
	num=malloc(128*3);
	sprintf(num,"%d%d%d%d%d%d%d%d%d",timeinfo->tm_sec,timeinfo->tm_min,timeinfo->tm_hour,timeinfo->tm_mday,timeinfo->tm_mon,timeinfo->tm_year,timeinfo->tm_wday,timeinfo->tm_yday,timeinfo->tm_isdst);
	return atof(num);
}

static char *salt;
static char *pass;
int done[2]={0,0};

static int parse_opt(int key,char *arg,struct argp_state *state){
	switch (key){
		case 'e':
			main1(arg);
			break;
		case 's':
			if ( done[0] == 0 ){
				salt=malloc(strlen(arg));
				strncpy(salt,arg,strlen(arg));
				done[0]=1;
			}
			break;
		case 'p':
			if ( done[1] == 0 ){
				pass=malloc(strlen(arg));
				strncpy(pass,arg,strlen(arg));
				done[1]=1;
			}
			break;
		case 'd':
			if ( done[0] == 0 ){
				salt=malloc(strlen(""));
				strncpy(salt,"",strlen(""));
			}
			if ( done[1] == 0 ){
				pass=malloc(strlen(""));
				strncpy(salt,"",strlen(""));
			}
			check(pass,salt);
			break;

	}
	return 0;	
}
int main (int argc, char **argv){
	struct argp_option options[]={
		{0,'e',"STRING",0,"password string for storage input"},
		{0,'p',"STRING",0,"password string reversal input"},
		{0,'s',"STRING",0,"for option 'p'; the salt string"},
		{0,'d',0,0,"run password verification"},	
		{0}
	};
	struct argp argp = {options,parse_opt};
	return argp_parse(&argp,argc,argv,0,0,0);
}
