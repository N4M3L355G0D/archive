#! /bin/bash

main() {
USER="$1"
if [ -z "$1" ] ; then
 read -rp "What is your GITHUB USER?" USER
elif [ "$1" == "-h" ] || [ "$1" == "--help" ] ; then
 echo -e "$0 <GITHUB USER>\n$0 -h||--help for help"
 exit
fi
mkdir "./gitrepos-$USER" && cd "./gitrepos-$USER"
PAGE=1; curl "https://api.github.com/users/$USER/repos?page=$PAGE&per_page=100" | grep -e git_url* | cut -d \" -f 4 | xargs -L1 git clone

}
main "$1"
