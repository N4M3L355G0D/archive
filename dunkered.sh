#! /usr/bin/env bash
#NoGuiLinux
#gpg user
User="Karl Josef Wisdom III"
endCode="#stop"
password=''
function banner(){
python2 << EOF
string="$1"
stringTop=len(string)*'-'
stringBot=len(string)*'='
print '{}\n{}\n{}'.format(stringTop,string,stringBot)
EOF
}

function checkDeps(){
	commands=("gzip" "gunzip" "base64" "gpg" "sed")
	allFail="no"
	missing=()
	counter=0
	for cmd in ${commands[@]} ; do
		export IFS=":"
		exist=''
		for pth in $PATH ; do
			if test -e "$pth/$cmd" ; then
				exist="yes"
			fi
		done
		export IFS=" "
		if test "$exist" == "" ; then
			missing[$counter]="$cmd"
			counter=`expr $counter + 1`
		fi
	done
	export IFS=" "
	if test "${#missing[@]}" -gt 0 ; then
		banner missing
		for miss in ${missing[@]} ; do
			echo -e "-> $miss"
		done
		return 1
	else
		return 0
	fi

}

function data(){
	acc=''
	message=''
	while test "$message" != "$endCode" ; do
		read -rp "TXT: " message
		acc="$acc\n""$message"
	done
	echo -e "$acc" | sed "s/$endCode$//"
}
function gzipData(){
	data | gzip - -f
}
function gpgData(){
	if test password == "" ; then
		gzipData | gpg -e -r "$User"
	else
		gzipData | gpg -c 
	fi
}
function b64Data(){
	gpgData | base64 -
}
function dataToXclip(){
	b64Data | xclip
}

function dataD(){
	acc=''
	message=''
	while test "$message" != "$endCode"; do
		read -rp "B64: " message
		acc="$acc""$message"
	done
	echo -e "$acc" | sed "s/$endCode$//"
}
function b64DataD(){
	dataD | base64 -d -
}
function gpgDataD(){
	if test "$password" == "" ; then
		b64DataD | gpg -d -r "$User"
	else
		b64DataD | gpg -d 
	fi
}
function gunzipData(){
	gpgDataD | gunzip -d - -f
}
function main(){
	if checkDeps ; then
		if test "$1" == "-e" ; then
			shift
			if test "$1" == "-s" ; then
				password="true"
			fi
			dataToXclip
		elif test "$1" == "-d" ; then
			shift
			if test "$1" == "-s" ; then
				password="true"
			fi
			gunzipData
		else
			echo -e "-d to decrypt\n-e to encrypt"
		fi
	else
		banner "Some dependencies do not appear to be in your \$PATH"
		exit 1
	fi
}
main "$@"
