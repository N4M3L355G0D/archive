#include <iostream>
#include <vector>
#include <string>

#define STRING "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","-","_","+","=","~","`","[","]","{","}","|","\\",":",";","\"","'",",","<",">",",",".","?","/" 

int main() 
{
	//std::vector<std::string> final{ "a", "b", "c" };
		std::vector<std::string> final{STRING};
	        std::vector<std::string> temp{STRING};

		    auto n = final.size();

		        final.resize( final.size() * temp.size() );

			    for ( auto i = n, j = final.size(); i != 0; --i )
				        {

						        for ( auto it = temp.rbegin(); it != temp.rend(); ++it )
								        {
										            final[--j] = final[i-1] + *it; 
											            }

							    }

			        for ( const auto &s : final ) std::cout << s << ' ';
				    std::cout << std::endl;

				        return 0;
}
