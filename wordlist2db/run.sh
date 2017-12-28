#! /bin/bash

cat temp1.txt | sed s\|"^"\|"python3 wordlist2db-insert.py "\|g | bash 
