mf1="test"
mf2='$6$wAn8dUwIB29ieair$WilBuVfVyZ0tM0.ue3WjpWb3P1pFQ2QrVuzwkDkN6Fq0Oj4OmttO1Aj1lDkwxG8Ha8nJfcA5a0kS4UghbwHOk1'
mf3=17530
mf4=0
mf5=99999
mf6=7

f1="$mf1"
f2="$mf3"
f3="$mf4"
f4="$mf5"
f5="$mf6"

sudo cat /etc/shadow | sed s\|"$mf1\:$mf2\:$mf3\:$mf4\:$mf5\:$mf6\:\:\:"\|"$f1\:`cat passwd.tmp`\:$f2\:$f3\:$f4\:$f5\:\:\:"\|g
