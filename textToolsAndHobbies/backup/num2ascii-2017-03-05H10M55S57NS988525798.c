#include <stdio.h>
#include <stdlib.h>

#define upper 126
#define lo 32
/* this program will be designated for the upper end of the 97 character character space */
int main(){
int hkill=40;
int prime[97]={0,};

/* start at the space char for all,
or if specific string initialize start from right to left with 
ascii int value, array must be same length as hkill value*/
/*
 "     %\=]" is equivalent to the start code below
 32 32 32 32 32 37 92 61 93 
*/

//int start[97]={32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32};
// initialize start to 32

//comment [ start ] if and uncomment above int start[97] for manual loop start
int start[97]={32,};
for ( int i=0 ; i < 97 ; i++ ){
 start[i]=32;
}
//comment [ end ]


for ( int a=start[0] ; a <= upper ; a++ ){ //97,1
 if (!( a < upper ) && (prime[0] == 0)){
  prime[0]=1;
  a=lo;
 }
 if ( hkill == 1 ) {
  printf("%c\n",a); 
 }
 else {
 for ( int b=start[1] ; b <= upper ; b++ ){ //96,2
  if (!( b < upper ) && (prime[1] == 0)){
   prime[1]=1;
   b=lo;
  }
  if ( hkill == 2 ) {
   printf("%c%c\n",a,b);
  }
  else {
  for ( int c=start[2] ; c <= upper ; c++ ){ //95,3
   if (!( c < upper ) && ( prime[2] == 0 )){
    prime[2]=1;
    c=lo;
   }
   if ( hkill == 3 ) {
    printf("%c%c%c\n",a,b,c);
   }
   else {
   for ( int d=start[3] ; d <= upper ; d++ ){ //94,4 
    if (!( d < upper ) && ( prime[3] == 0 )){
     prime[3]=1;
     d=lo;
    }
    if ( hkill == 4 ) {
     printf("%c%c%c%c\n",a,b,c,d);
    }
    else {
    for ( int e=start[4] ; e <= upper ; e++ ){ //93,5
     if (!( e < upper ) && ( prime[4] == 0 )){
      prime[4]=1;
      e=lo;
     }
     if ( hkill == 5 ) {
      printf("%c%c%c%c%c\n",a,b,c,d,e);
     }
     else {
     for ( int f=start[5] ; f <= upper ; f++ ){ //92,6
      if (!( f < upper ) && ( prime[5] == 0 )){
       prime[5]=1;
       f=lo;
      }
      if ( hkill == 6 ) {
        printf("%c%c%c%c%c%c\n",a,b,c,d,e,f);
      } 
      else {
      for ( int g=start[6] ; g <= upper ; g++ ){ //91,7
       if (!( g < upper ) && ( prime[6] == 0)){
        prime[6]=1;
        g=lo;
       }
       if ( hkill == 7 ) { /**/
        printf("%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g);
       }
       else { /**/
        for ( int h=start[7] ; h <= upper ; h++ ){ //90,8
         if (!( h < upper ) && (prime[7] == 0)){
          prime[7]=1;
          h=lo;
         }
         if ( hkill == 8 ) {
          printf("%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h);
         }
         else {
          for ( int i=start[8]; i <= upper ; i++ ){ //90,9
           if (!( i < upper) && (prime[8] == 0)) {
            prime[8]=1;
            i=lo;
           }
           if ( hkill == 9 ) {
           printf("%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i);
           }
           else {
            for ( int j=start[9] ; j <= upper ; j++ ){ // 89,10
             if (!( j < upper) && (prime[9] == 0)) {
              prime[9]=1;
              j=lo;
             }
             if ( hkill == 10 ) {
              printf("%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j);
             }
             else {
              for ( int k=start[10] ; k <= upper ; k++ ){ // 88,11
               if (!( k < upper ) && (prime[10] == 0)){
                prime[10]=1;
                k=lo;
               }
               if ( hkill == 11 ) {
                printf("%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k);
               }
               else {
                for ( int l=start[11] ; l <= upper ; l++ ){ //87,12
                 if (!( l < upper ) && (prime[11] == 0 )){
                  prime[11]=1;
                  l=lo;
                 }
                 if ( hkill == 12 ) {
                  printf("%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l);
                 }
                 else {
                  for ( int m=start[12] ; m <= upper ; m++ ){ //86,13
                   if (!( m < upper ) && (prime[12] == 0 )){
                    prime[12]=1;
                    m=lo;
                   }
                   if ( hkill == 13 ) {
                    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m);
                   }
                   else {
                    for ( int n=start[13] ; n <= upper ; n++ ){ //85,13
                     if (!( n < upper ) && ( prime[13] == 0 )){
                      prime[13]=1;
                      n=lo;
                     }
                     if ( hkill == 14 ) {
                      printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n);
                     }
                     else {
                      for ( int o=start[14] ; o <= upper ; o++ ){ //84,14
                       if (!( o < upper ) && (prime[14] == 0 )){
                        prime[14]=1;
                        o=lo;
                       }
                       if ( hkill == 15 ) {
			printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o);
                       }
                       else {
                        for (int p=start[15] ; p <= upper ; p++) { //83,15
      			 if (!( o < upper ) && (prime[15] == 0 )) {
                          prime[15]=1;
                          p=lo;
                         }
			 if (hkill == 16) {
                          printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p);
                         }
			 else {
			  for (int q=start[16] ; q <= upper ; q++) {
			   if (!( q < upper ) && (prime[16] == 0 )){
			    prime[16]=1;
			    q=lo;
			   }
			   if ( hkill == 17){
			    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q);
			   }
                           else {
			    for ( int r=start[17] ; r <= upper ; r++) {
			     if (!( r < upper ) && (prime[17] == 0 )) {
                              prime[17]=1;
   			      r=lo;
	                     }
  			     if ( hkill == 18) {
                              printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r);
			     }
   		             else {
			      for ( int s=start[18] ; s <= upper ; s++) {
                               if (!( s < upper ) && (prime[18] == 0 )) {
                                prime[18]=1;
                                s=lo;
			       }
			       if ( hkill == 19 ) {
				printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s);
			       }
			       else {
			        for ( int t=start[19] ; t <= upper ; t++) {
			         if (!( t < upper ) && ( prime[19] == 0)) {
			 	  prime[19]=1;
			 	  t=lo;
				 }
				 if ( hkill == 20) {
				  printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t);
				 }
                                 else {
                                  for ( int u=start[20] ; u <= upper ; u++ ) {
                                   if (!( u < upper ) && ( prime[20] == 0 )) { 
                                    prime[20]=1;
                                    u=lo;
                                   }
                                   if (hkill == 21){
                                     printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u);
                                   }
				   else {
				    for ( int v=start[21] ; v <= upper ; v++){
                                      if (!( v < upper ) && (prime[21] == 0 )) {
				       prime[21]=1;
				       v=lo;
				      }
				      if ( hkill == 22) {
				       printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v);
				      }
				      else {
				       for (int w=start[22] ; w <= upper ; w++) {
					if (!( w < upper ) && (prime[22] == 0)){
					 prime[22]=1;
					 w=lo;
					}
					if (hkill == 23) {
					 printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w);
					}
					else {
					 for (int x=start[23] ; x <= upper ; x++ ){
					  if (!( x < upper ) && ( prime[23] == 0 )){
					   prime[23]=1;
					   x=lo;
                                          }
					  if (hkill == 24){
					   printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x);
					  }
                                          else {
                                           for ( int y=start[24] ; y <= upper ; y++ ){
                                            if (!( y < upper ) && (prime[24] == 0)) {
                                             prime[24]=1;
                                             y=lo;
                                            }
                                            if ( hkill == 25 ) {
					     printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y);
					    }
                                            else {
                                             for ( int z=start[25] ; z <= upper ; z++ ){
                                              if (!(z < upper ) && (prime[25] == 0)){
					       prime[25]=1;
                                               z=lo;
                                              }
                                              if (hkill == 26){
                                               printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z);
					      }
					      else {
					       for ( int aA=start[26] ; aA <= upper ; aA++){      
					        if (!( aA < upper ) && ( prime[26] == 0 )){
						 prime[26]=1;
						 aA=lo;
					        }
					        if (hkill == 27){
						 printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA);
					        }
						else {
						for ( int aB=start[27] ; aB <= upper ; aB++ ){
						 if (!( aB < upper ) && ( prime[27] == 0)){
						   prime[27]=1;
						   aB=lo;
						  }
						 if (hkill == 28) {
					          printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB);
						  }
						 else {
						  for ( int aC=start[28] ; aC <= upper ; aC++ ){
						   if (!( aC < upper ) && ( prime[28] == 0)){
						    prime[28]=1;
						    aC=lo;
						   }
						   if ( hkill == 29 ) {
						    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC);
						   }
						   else {
						    for ( int aD=start[29] ; aD <= upper ; aD++ ){
						     if (!( aD < upper ) && ( prime[29] == 0 )) {
						      prime[29]=1;
						      aD=lo;
						     }
						     if ( hkill == 30 ) {
						      printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD);
						     }
						     else {
						      for ( int aE=start[30] ; aE <= upper ; aE++ ){
						       if (!( aE < upper ) && ( prime[30] == 0 )) {
							prime[30]=1;
							aE=lo;
						       }
						       if ( hkill == 31 ) {
							printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD,aE);
						       }
						       else {
							for ( int aF=start[31] ; aF <= upper ; aF++){
							 if (!( aF < upper ) && ( prime[31] == 0 )){
							  prime[31]=1;
							  aF=lo;
							 }
							 if ( hkill == 32 ) {
							  printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD,aE,aF);
							 }
							 else {
							  for ( int aG=start[32] ; aG <= upper ; aG++ ) {
							   if (!( aG < upper ) && (prime[32] == 0 )){
							    prime[32]=1;
							    aG=lo;
							   }
							   if ( hkill == 33 ) {
							    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD,aE,aF,aG);
							   }
							   else {
							    for ( int aH=start[33]; aH <= upper ; aH++ ) {
							     if (!(aH < upper ) && (prime[33] == 0 )){
							      prime[33]=1;
							      aH=lo;
							     }
							     if ( hkill == 34 ){
							      printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD,aE,aF,aG,aH);
							     }
							     else {
							      for ( int aI=start[34] ; aI <= upper ; aI++){
							       if (!( aI < upper ) && ( prime[34] == 0 )){
								prime[34]=1;
								aI=lo;
							       }
							       if (hkill == 35){
							        printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD,aE,aF,aG,aH,aI);
							       }
							       else {
								for ( int aJ=start[35] ; aJ <= upper ; aJ++){
								 if (!( aJ < upper ) && ( prime[35] == 0 )){
								  prime[35]=1;
								  aJ=lo;
								 }
								 if ( hkill == 36 ) {
								  printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD,aE,aF,aG,aH,aI,aJ);
								 }
								 else {
								  for ( int aK=start[36] ; aK <= upper ; aK++){
								   if (!( aK < upper ) && ( prime[36] == 0 )){
								    prime[36]=1;
								    aK=lo;
								   }
								   if (hkill == 37) {
								    printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD,aE,aF,aG,aH,aI,aJ,aK);
								   }
								   else {
								    for ( int aL=start[37] ; aL <= upper ; aL++){
								     if (!( aL < upper ) && ( prime[37] == 0 )) {
								      prime[37]=1;
								      aL=lo;
								     }
								     if (hkill == 38){
								      printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD,aE,aF,aG,aH,aI,aJ,aK,aL);
								     }
								     else {
								      for ( int aM=start[38] ; aM <= upper ; aM++ ){
								       if (!( aM < upper ) && ( prime[38] == 0 )){
									prime[38]=1;
									aM=lo;
								       }
								       if (hkill == 39 ) {
									printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD,aE,aF,aG,aH,aI,aJ,aK,aL,aM);
								       }
								       else {
									for ( int aN=start[39] ; aN <= upper ; aN++ ){
								         if (!( aN < upper ) && ( prime[39] == 0 )){
									  prime[39]=1;
									  aN=lo;
									 }
									 if ( hkill == 40 ) {
									  printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aA,aB,aC,aD,aE,aF,aG,aH,aI,aJ,aK,aL,aM,aN);
									 }
									 //here
									}
								       }
								       /*3-5-2017 @ 10:55 am*///here
								      }
								     }
								     /*ignore 3-5-2017 @ 10:48 am*///here
								    }
								   }
								   /*ignore 3-5-2017 @ 10:40 am*///here
								  }
								 }
								 /*ignore 3-5-2017 @ 10:24 am*///here
								}
							       }
							       /*ignore 3-5-2017 @ 10:33 am*///here
							      }
							     }
							     /*ignore 3-5-2017 @ 10:03 am*///here
							    }
							   }
							   /*ignore 3-5-2017 @ 9:57 am*///here
							  }
							 }
							 /*ignore 3-5-2017 @ 9:49 am*///here
							}
						       }
						       /*3-4-2017 @ 2:12 pm*///here
						      }
						     }
						     /*ignore 3-4-2017 @ 1:20 pm*///here
						    }
						   }
						   /*ignore 3-4-2017 @ 12:46 pm*///here
						  }
						 }
						/*ignore 3-4-2017 @ 12:20 pm*/ //here
						 }
						}
					       /*ignore 3-4-2017 @ 3:18 am*///here
					       }
					      }
                                              /*ignore 3-4-2017 @ 2:39 am*///here
                                             }
                                            }
                                            /*ignore 2-27-2017 @ 12:10am*///here
                                           } 
                                          }
					/*ignore 2-27-2017 @ 12:00 am*/ //here
					 }
					}
					/*ignore 2-26-2017 @ 8:00 am*///here
				       }
				      }
				      /*ignore 2-26-2017 @ 5:27 am*///here
				    }
			           }
				   /* ignore 2-26-2017 @ 5:17 am*///here
                                  }
                                 }
                                 /*ignore 2-23-2017 @ *///here
                                }
                               }
			      }
			      /*ignore 2-23-2017 @ 9:50 pm*///here
			     }
			     /*ignore 2-23-2017 @ 9:32 pm*///here
			    }
			   }
                           /* ignore 2-23-2017 @ 9:18 pm*///here
			  }
			 }
                         /*ignore 2-23-2017 @ 9:01 pm*/ //here
                        }
		       }
                       /* ignore 2-23-2017 @ 8:50 pm*/ //here
                      }
                     }
                    }
                   }
                  }
	         }
                }
               }
              }
             }
            }
           }
          }
         }
        } /**/ } /**/ } /**/ } /**/ } /**/ } /**/ }
       }
      }
     }
    }
   }
  }
 }
}


}
