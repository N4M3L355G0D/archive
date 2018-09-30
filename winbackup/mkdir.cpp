#include <sys/stat.h>
#include <iostream>

using namespace std;

int main(int argc,char** argv){
	if (argc >= 2) {
		const int dir_err = mkdir(argv[1],S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
		if ( dir_err == -1 ){
			cout << "error making directory" << "\n";
		}
	}
}
