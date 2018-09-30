#! /usr/bin/env bash
#noguilinux

#get tar elements/nodes by linenumber

function header(){
python2 << EOF
iString='$1'
bars='='*len(iString)
print bars+'\n'+iString+'\n'+bars
EOF
}

function getNodeByLineNum(){
	if test "$1" != "" ; then
		if test -e "$1" ; then
			if test -f "$1" ; then
				file="$1"
				shift
				if test "$1" != ""; then
					line="$1"	
					tar --list --file "$file" --to-stdout |& nl | tr -d " " | sed 's/\t/# /' | sed 's/^/#/' | grep -w "#$line#" | cut -f2 -d" "
				else
					header "$file"
					tar --list --file "$file" --to-stdout |& nl | tr -d " " | sed 's/\t/# /' | sed 's/^/#/'
				fi
			else
				header "fname given is not a file"
			fi
		else
			header "file does not exist!"
		fi
	else
		header "fname cannot be blank!"
	fi
}
getNodeByLineNum "$@"
