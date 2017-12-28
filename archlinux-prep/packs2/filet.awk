#! /usr/bin/awk -f

{
print "if [ \"`pacman -Qqe " $1 "`\" != '" $1 "' ] ; then";
print "\tyaourt -S " $1;
print "\tif [ $? == 0 ] ; then";
print "\t\techo \"" $1 ": installed\"";
print "\telse";
print "\t\techo \"" $1 ": !not installed: install failure\"";
print "\tfi";
print "else";
print "\techo \"" $1 ": !installed as already installed.\"";
print "fi";
	}
