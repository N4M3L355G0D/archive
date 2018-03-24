#! /usr/bin/env bash
#NoGuiLinux
pkgDetailsDir='./pkgDetails'

function xmlGen(){
	printf "<master host='%s'>\n" "$HOST"
	cat "$pkgDetailsDir"/*.xml
	printf "</master>\n"

}
xmlGen
