to create the nextgearxx.txt mostly inclusive WPA wordlist for cracking default NetgearXX passwords that have not been changed, do:

/usr/bin/python3 netgearxx.py --file

#this will generate the text file as well

/usr/bin/python3 netgearxx.py --stdout > netgearxx.txt

#use your preference, stdout was placed there for viewing purposes only.

the final file netgearxx.txt will require 635 GB of HDD storage space 

the wordsplit.sh script is not yet complete, but will require another 635 GB of starage if you want to chunk netgearxx.txt for several hosts. Due to the size of this file, operations that require looking at the length of the file and its contents will take a LONG time to complete.

I am not packing the netgearxx.txt for obvious reasons, that is why i have provided the scripts to generate the file on your own disk. Again, generating the file will take a long time... a 4 Core i3 at 4.28 GHZ took roughly 12 hours to complete the task, so be prepared. 

count.py is for counting the lines of the file, and printing the final count. you should really use `wc -l` instead, but here is anyways.

nouns.txt contains the nouns required by netgearxx.py
adjectives.txt contains the adjectives required by netgearxx.py
three end of string numbers are generated within netgearxx.py

if you have any other questions... please contact me at k.j.hirner.wisdom@gmail.com

for cracking purposes, use hashcat with a decent nvidia card to speed the cracking speed, and maybe even cluster multiple linux systems using the generated chunks from wordsplit.sh.

Best of Cracking, Hackit.
