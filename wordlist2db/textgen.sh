#! /bin/bash


bash filter.sh > tmp1
cat tmp1 | sed s\|"^'"\|""\|g | sed s\|"'$"\|""\|g | python3 size.py > text.tmp
python order.py > final.txt

cat final.txt | sed s\|"^"\|"'"\|g | sed s\|"$"\|"'"\|g > temp1.txt 
cat final.txt > text1.tmp
rm tmp1 text.tmp final.txt
