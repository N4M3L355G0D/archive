loop.c - generate strings src
	will add the ability to start from a certain string later
	this code is not fully mine; rather, it is adapted from http://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/, with certain modifications, listed below.
		global integer
		 to count the times a function is executed
		for-loop in main()
		 allowing for the printing of multiple characterspaces
		STRING macro
		 defines all characters to be used in generator
		2nd printf statement now includes " |:| %d \n"
		 to print line number from global integer
loop - 64 bit binary of the above source code, compiled with GNU GCC ( bash command g++ loop.c -o loop -fpermissive ), on Manjaro Linux (x64,but that should be obvious,as 64 bit runs only on a minimum of x64 )

NoGuiLinux 
