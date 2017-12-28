filter(){
	find mount/ -iname "*.txt" | grep -v "SecLists/Usernames" | \
       	grep -v "SecLists/Payloads" | grep -v "SecLists/Fuzzing" | \
	grep -v "SecLists/Pattern_Matching" | \
	grep -v "SecLists/IOCs" | grep -v "SecLists/Discovery" | \
	grep -v "SecLists/Miscellaneous" | grep -v "JohnTheRipper" | \
        grep -v "READ.ME.!!.txt" | grep -v "readme.txt" | sed s\|"^"\|"'"\|g | sed s\|"$"\|"'"\|g

}
filter

#text(){

#filter | xargs --delimiter="\n" ls -l | awk '{print $5 "<+>" $9}' 
#}
#text
