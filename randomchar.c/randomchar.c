#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
//#include <time.h>
#include <sodium.h> //provides randombytes functions
#include <string.h> 
#include <math.h> // provides pow()
#include <argp.h> // cmd args

int gen(int base);

static int parse_opt(int key, char *arg, struct argp_state *state){
 switch(key){
	 case 'l':{
		 gen(atoi(arg));
		 break;
		  }
	}
 return 0;
}

int gen(int base){

	char string[128];
	uint32_t myInt;

	randombytes_buf(string,128);
	int exp=1; //in case of needing an oversized string, exponent
	//int base; //in case of needing an oversized string, base

	int n=pow(base,exp); //resulting output string size
	
	char outstring[n]; 
	for ( int i = 0 ; i < n ; i++ ){
		outstring[i]=randombytes_uniform(127);
		/*in the event the character output is not 32 or greater, run the below*/
		while ( outstring[i] < 32 ){
			outstring[i]=randombytes_uniform(127);
		}
		printf("%c",outstring[i]);
	}
	printf("\n");
}

int main(int argc, char **argv){
 if ( argc < 2 ){
  gen(8);
 }
 else {
 struct argp_option options[]={
	{0,'l',"NUM",0,"length of outstring"},
	{0}
 };
 struct argp argp = { options,parse_opt,0,0};
 return argp_parse(&argp,argc,argv,0,0,0);
 }
}
