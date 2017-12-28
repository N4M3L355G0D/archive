// Program to print all combination of size r in an array of size n
#include<stdio.h>
#define STRING "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","-","_","+","=","~","`","[","]","{","}","|","\\",":",";","\"","'",",","<",">",",",".","?","/"," " 

int linen=0;

void combinationUtil(int arr[],int n,int r,int index,int data[],int i);

// The main function that prints all combinations of size r
// in arr[] of size n. This function mainly uses combinationUtil()
void printCombination(int arr[], int n, int r)
{
	// A temporary array to store all combination one by one
	int data[r];

	// Print all combination using temprary array 'data[]'
	combinationUtil(arr, n, r, 0, data, 0);
}

/* arr[] ---> Input Array
n	 ---> Size of input array
r	 ---> Size of a combination to be printed
index ---> Current index in data[]
data[] ---> Temporary array to store current combination
i	 ---> index of current element in arr[]	 */
void combinationUtil(int arr[], int n, int r, int index, int data[], int i)
{
	//count the times of function execution
	linen++;
	// Current cobination is ready, print it
	if (index == r)
	{
		for (int j=0 ; j<r; j++ ){
			printf("%s",data[j]);
		}
		// linen/2 is due to double function execution below
		printf(" |:| %d \n",linen/2);
		return;
	}

	// When no more elements are there to put in data[]
	if (i >= n)
		return;

	// current is included, put next at next location
	data[index] = arr[i];
	combinationUtil(arr, n, r, index+1, data, i+1);
        
	// current is excluded, replace it with next (Note that
	// i+1 is passed, but index is not changed)
	combinationUtil(arr, n, r, index, data, i+1);
}

// Driver program to test above functions
int main()
{
	int arr[] = {STRING};
	int r = 63;
	for ( int x = 1; x <= r ; x++ ){ 
	int n = sizeof(arr)/sizeof(arr[0]);
		printCombination(arr, n, x);
	}
	return 0;
}
