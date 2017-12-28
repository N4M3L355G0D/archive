#! /usr/bin/awk -f

{
	print "if [ \"`pacman -Qqe " $1 "`\" != '" $1 "' ] ; then";
	print "\tsudo pacman -S " $1;
	print "\techo \"" $1 ": installed\"";
	print "else"
	print "\techo \"" $1 ": !installed as already installed.\"";
	print "fi";
}
