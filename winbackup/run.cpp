#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
using namespace std;
class one {

	public:
	string cmd="";
	string nocfg="no";
	string CFG="cmds.txt";

	int cfgExists(string cfg){
		ifstream CFG(cfg);
		return CFG.good();
	}
	string getOptions(string line,string options,string displayLines){
	//get config options to save in public
			std::vector<string> v;
			stringstream acc(line);
			string item;
			//split current line by equals
			while(getline(acc,item,'=')){
				v.push_back(item);
			}
			if ( displayLines == "yes" ){
				//print contents from current vector
				cout << v[0] << v[1] << "\n";
			}
			if ( v[0] == options ){
				return v[1];
			} else {
				return "noCmd";
			}
	}
	void readCfg(string displayLines){
		if (cfgExists(CFG)){
			ifstream config (CFG);
			string line = "";
			//get line from file
			while (getline(config,line)){
				cmd=getOptions(line,"cmd",displayLines);
			}
			config.close();
		} else {
			nocfg="yes";
		}
	}
	int runCmd(string cmdLocal){
		int bufsize=1024;
		char buff[bufsize];
		FILE *fp = popen(cmdLocal.c_str(),"r");
		while ( fgets(buff,bufsize,fp ) != NULL){
			printf("%s",buff);
		}
		pclose(fp);
	}
	int run(int argc,char** argv){
		if ( argc >= 2 ){
			cmd=argv[1];
			runCmd(cmd);
		} else {
			printf("%s\n","command arg not provided on cmdline, using cfg");
			readCfg("no");
			runCmd(cmd);
		}
	}
} obj;
int main(int argc, char** argv){
	obj.run(argc,argv);
	if ( obj.nocfg == "no" ){
		cout << "cmd_execute: " << obj.cmd << "\n";
	} else {
		cout << "no config '" << obj.CFG << "' available\n";
	}
}
