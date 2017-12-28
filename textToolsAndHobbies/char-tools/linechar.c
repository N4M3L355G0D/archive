#include <stdio.h>

#include "stringparser.h"
#define lo 32
#define upper 127

int main(){
	unsigned long count=0;
	int prime[2]={0,0};
	int hkill=2;
	char *str=COMPLETE;
	for ( int a=lo ; a < upper ; a++ ){
		if (!( a < upper ) && ( prime[0] == 0 )){
		prime[0]=1;
		a=lo;
		}
		if ( hkill == 1 ){
			if ( hkill != 1 ){
			printf("%c\n",a);
			}
			else if ( hkill == 1 ){
			printf("LINENUMBER:%lu %c\n",count,a);
			}
			count++;
		}
		else{
			for ( int b=lo ; b < upper ; b++ ){
				if (!( b < upper ) && (prime[1] ==0)){
				prime[1]=1;
				b=lo;
				}
				if ( hkill == 2 ){
				printf("LINENUMBER:%lu %c%c\n",count,a,b);
				count++;
				}
				else {
					printf("%c%c\n",count,a,b);
				}
			}
		}

						

	}

}
