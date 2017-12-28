$NAME == variable, using bash syntax
Format Template
==================
script
	useage
	
	use
==================
userPath.awk
	cat /etc/passwd | userPath.awk who=git
	./userPath.awk who=git /etc/passwd

	parse /etc/passwd to extract users and their paths
	the $who, variable, is to extract an exact user and not the whole file

gaddress.awk
	./gaddress.awk term=$TERM opt_fields=$OPTIONAL_FIELD fieldCheck="no||yes" $FILE 
	
	extract emails from google.csv, which was exported from contacts.google.com
