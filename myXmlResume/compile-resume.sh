#! /usr/bin/env bash
#NoGuiLinux

function datecode(){
	date +H%HM%MS%Smm%mdd%dyy%Y
}

function resume {
       	echo '<resume>' 
	cat resume.xml | sed s/^/'\t'/g 
	cat schools.xml | sed s/^/'\t'/g 
	cat references.xml | sed s/^/'\t'/g 
	echo '</resume>' 
}
function main(){
	resume | xmllint --format - | sed s/'\t'/'  '/g | sed s/'&#xA0;'/''/g > resume-`datecode`.xml
}
main
