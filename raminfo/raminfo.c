#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <ctype.h>
#include <sodium.h>
#include <string.h> 

int main(){


	FILE *memfile;
	unsigned int counter=0;
	char c;
	char *data= (char*)malloc(1);
	//we open up initially to set malloc size
	memfile=fopen("/proc/meminfo","r");
	while ( (c=fgetc(memfile)) != EOF ) {
         //printf("%c",c);
	 //while here generate size for malloc()
	 counter++;
	}
	//we close the memfile, as it is now at the EOF
	fclose(memfile);
	//start a data counter to set char in data[]
        int cty=0;
	//realloc data to counter size, which according to some sources, unsigned int is close to size_t
	data=realloc(data,counter);
	//reopen file to cp into memory
        memfile=fopen("/proc/meminfo","r");
	while (( c=fgetc(memfile)) != EOF){
		data[cty]=c;
		cty++;
	}
	//now cp'd into mem
	//lets print the data in mem
	for ( int i=0; i < counter ; i++ ){
         printf("%c",data[i]);
	}
	return 0;

}
