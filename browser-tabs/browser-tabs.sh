#! /bin/bash
## variable setup 
urls=()
cmd_in="@" ## urls variable
y=1
x=0
browser=google-chrome-stable

## get overide variables from configuration

## adds the urls to urls array
urls_num1=`echo "$@" | grep -o " " | wc -l`
while (( $y <= $(expr $urls_num1 + 1 ) )) ; do
 url=`echo "$@" | cut -f$y -d" "`
 y=`expr $y + 1`
 urls+=($url)
done

urls_num=${#urls[@]}

## begin command execution

echo -e "\n\n"
while (( $x < $urls_num )) ; do
 $browser ${urls[$x]} &
 x=`expr $x + 1`
done
