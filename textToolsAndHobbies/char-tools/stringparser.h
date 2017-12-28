#include <stdio.h>
#include <stdlib.h>
#include <argp.h>
#include <string.h>

#define SPECIAL "~!@#$%^&*()_+`-=[]\\{}|;:\"<>?,./ "
#define ALPHAL "abcdefghijklmnopqrstuvwxyz"
#define ALPHAC "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
#define NUMERIC "1234567890"
#define COMPLETE "~!@#$%^&*()_+`-=[]\\{}|;:\"<>?,./ abcdefghijklmnopqrstuvwxyzABDCEFGHIJKLMNOPQRSTUVWXYZ1234567890"

//add a printf suppressor bool
char* stringparser(char *String,int suppress){
 int count=0;
 for ( int i=0 ; String[i] != NULL ; i++ ){
  count++;
 }
 if ( suppress != 1) {
  //set string for testing
  //print contents, charnumber, ascii val to stdout
  printf("DATA TRANSLATION:\n");
  for ( int i=0 ; String[i] != NULL ; i++ ){
  	printf("\t%d %d %c\n",i,String[i],String[i]);
  }
  //print format key
  printf("COLUMN_FORMAT:\n\tCH# OSAV OSAC\nwhere:\n\tCH# - Character Number of the string starting at 0\n\tOSAV - output string ASCII value\n\tOSAC - output string ASCII character\n");
  //return convert char pointer for use elsewhere
 }
 if ( count <= 97){
  String=String;
 }
 else {
  String="OVER_97_CHAR";
 }
 return String;
}

