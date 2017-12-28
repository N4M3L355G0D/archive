#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

/* these make coding easier, since all I have to do is use the defined segments, due to the portion of code being used is the same within the selection system */
#define SIZE 3
#define print() printf("%s >> %s <<\n",data.choice,data.input)
#define loop() 	for ( int i=1 ; i <= SIZE-1 ; i++ )\
					{\
						printf("%s %d : ",data.request_1,i);\
						scanf("%lf",&data.numeric[i]);\
					} 
/* the area that I use to store my stuff, and pass to the appropriate functions. */


struct mem{
	double array[128];
	char request_0[128];
	char warning_0[128];
	char request_1[128];
	char help_0[128];
	char separator[128];
	char choice[32];
	char solution[32];
	char input[5];
	
	
	double numeric[SIZE];

	};

/* my function prototypes return double to assist with accuracy */
double add(struct mem data);
double sub(struct mem data);
double mul(struct mem data);
double divide(struct mem data);
double modulus(struct mem data);

/* please not that I have written this piece to have as few bugs/errors as possible. as such, I have included specific statements to prevent undesirable output.
if you still see something, please let me know at k.j.hirner.wisdom@gmail.com, or text at 804-489-0791. Thank you. */
int main()
{
	struct mem data; //declares the struct mem as object data

	/*the section below passes the required strings into the object data */

	strcpy(data.request_1,"Please enter value");
	strcpy(data.help_0,"add = addition, sub = substraction, div = division, mul = multiplication, mod = modulus, ? = help, q = quit");
	strcpy(data.separator,"																");
	strcpy(data.request_0, "What operation would you like to perform? [ Otherwise, type 'q' to quit or '?' for help ] : ");
	strcpy(data.warning_0,"That is an incorrect operation, or is currently unavailable. Please try something else.");
	strcpy(data.choice,"You selected ");
	strcpy(data.solution,"The Solution is ");

/*the section of code is where the work begins. I have used #defines to reduce the amount of keyboard-work to as little as possible and to increase readability.*/

	while  ( strcmp("q",data.input) != 0 ) 
		{
			
			printf("%s",data.request_0);

			scanf("%s",&data.input);
	
			if ( strcmp("add",data.input) == 0 ) // addition
				{
				print(); //please refer to the define's above
				loop(); //please refer to the defines's above
				printf("%s %0.2lf.\n",data.solution,add(data));
				}
			else if ( strcmp("sub",data.input) == 0 ) // subtraction
				{
				print();
				loop();	
				printf("%s %0.2lf.\n",data.solution,sub(data));
				}
			else if ( strcmp("div",data.input) == 0 ) // division
				{
				print();
				loop();
				printf("%s %0.2lf.\n",data.solution,divide(data));
				}
			else if ( strcmp("mul",data.input) == 0 ) // multiplication
				{
				print();
				loop();	
				printf("%s %0.2lf.\n",data.solution,mul(data));
				}
			else if ( strcmp("mod",data.input) == 0 ) // floating point modulus
				{
				print();
				loop();	
				printf("%s %0.2lf.\n",data.solution,modulus(data));
				}
			else if ( strcmp("q",data.input) == 0 ) // keeps the loop from using any other options
				{
					system("exit");
				}
			else if ( strcmp("?",data.input) == 0 ) // the help menu
				{
				printf("%s\n",data.separator);
				printf("%s\n",data.help_0);
				printf("%s\n",data.separator);
				}
			else
				{
				printf("%s\n",data.warning_0);
				}
		
	
	}			
}

/* here are the functions that perform the work. The main function passes the struct memory to the appropriate function as the object data, so that the calculations may be performed. */

double add(struct mem data)
{
	data.numeric[0] = data.numeric[1] + data.numeric[2];
	return data.numeric[0];
}
double sub(struct mem data)
{
	data.numeric[0] = data.numeric[1] - data.numeric[2];
	return data.numeric[0];
}
double mul(struct mem data)
{
	data.numeric[0] = data.numeric[1] * data.numeric[2];
	return data.numeric[0];
}
double divide(struct mem data)
{
	data.numeric[0] = data.numeric[1] / data.numeric[2];
	return data.numeric[0];
}
double modulus(struct mem data)
{
	data.numeric[0] = fmod(data.numeric[1],data.numeric[2]);
	return data.numeric[0];
}
/*end of the 'vierus calculator' */
