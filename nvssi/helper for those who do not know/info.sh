#! /bin/bash

path=/usr/bin/
browser="$path"google-chrome-stable

#if you are on debian, change browser to iceweasel, or midori. If you have google-chrome installed, you use that instead. this is to bring up some git helper pages that helped me. if you can find them before they dissapear. if they are gone by the time you find this in you code contact me and i will relay a pdf copy of those pages to you. i can be contacted at k.j.hirner.wisdom@gmail.com, subject line 'nvssi helper'.

if [ -e $browser ] ; then
	$browser https://help.github.com/articles/generating-ssh-keys/ &> /dev/null & 
	$browser http://stackoverflow.com/questions/4658606/import-existing-source-code-to-github &> /dev/null &
fi
