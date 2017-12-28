#! /usr/bin/python3
#get total bytes of data being operated on

raised(){
/usr/bin/python3 << EOF
import math

a=$1
b=$2

c=a/(b*(math.pow(10,6)))
print(int(c))

EOF
}

rate=55
total=`bash filter.sh | sed s\|"^'"\|""\|g | sed s\|"'$"\|""\|g | python3 size.py | ./add.awk `
period=`raised $total $rate`
echo $total
echo "at a rate of $rate MB per day the current task will complete in $period days, or roughly `expr $period \/ 365` years."
