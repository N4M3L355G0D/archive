#! /usr/bin/env bash
#NoGuiLinux
#check for dependencies for bash/sh scripts

function banner(){
python2 << EOF
string="$1"
stringTop=len(string)*'-'
stringBot=len(string)*'='
print '{}\n{}\n{}'.format(stringTop,string,stringBot)
EOF
}

function checkDeps(){
        allFail="no"
	commands=()
        missing=()
        counter=0
	for load in "$@" ; do
		commands["$counter"]="$load"
		counter="`expr $counter + 1`"
	done
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
checkDeps "$@"
