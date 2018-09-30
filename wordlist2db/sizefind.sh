filter(){
	find wlwa/ -iname "*.txt" -size +50M | grep -v "SecLists/Usernames" | \
       	grep -v "SecLists/Payloads" | grep -v "SecLists/Fuzzing" | \
	grep -v "SecLists/Pattern_Matching" | \
	grep -v "SecLists/IOCs" | grep -v "SecLists/Discovery" | \
	grep -v "SecLists/Miscellaneous" | grep -v "JohnTheRipper" | \
        grep -v "READ.ME.!!.txt" | grep -v "readme.txt" 

}
filter | tee sizefind.log
