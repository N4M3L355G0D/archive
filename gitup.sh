git add .

if [ -z "$1" ] ; then
	MSG="DEFAULT"
else
	MSG="$1"
fi

git commit -a -m "$MSG"

git push
