#include "stringparser.h"

int main1(char *in){
	char *a;
	a=stringparser(in,0);
	printf("INPUT: %s\n",a);
}

static int parse_opt(int key, char *arg,struct argp_state *state){
	switch(key){
		case 'i':
			{
			main1(arg);
			break;
			}
		case 's':
			main1(SPECIAL);
			break;
		case 'A':
			main1(ALPHAC);
			break;
		case 'a':
			main1(ALPHAL);
			break;
		case 'n':
			main1(NUMERIC);
			break;
		case 'f':
			main1(COMPLETE);
			break;
	}
	return 0;
}
int main(int argc, char **argv){
	struct argp_option options[]={
		{"input",'i',"STRING",0,"input string"},
		{"predefined-special",'s',0,0,"predefined special string"},
		{"predefined-alpha-caps",'A',0,0,"predefined alpha-cap character string"},
		{"predefined-alpha-lower",'a',0,0,"predefined alpha-lower character string"},
		{"predefined-numeric",'n',0,0,"predefined numeric character string"},
		{"prefedined-ascii-full",'f',0,0,"predefined ascii set"},
		{0}
	};
	struct argp argp = {options,parse_opt,0,0};
	argp_parse(&argp,argc,argv,0,0,0);
}
