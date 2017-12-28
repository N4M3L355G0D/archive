algo() {
bc << EOF

scale=2
profit=$1
percent_tax=0.14
percent_hours_offset=0.02


profit-(profit*(percent_tax+percent_hours_offset))

EOF

}

helper() {
cat << EOF
please enter a value
====================
$0 <income calculated from income.py>
WARNING: THIS IS ONLY TO GET A ROUGH AVERAGE OF GROSS INCOME AFTER TAX
WARNING 2: I AM NOT AN INCOME EXPERT; THIS IS JUST BUILT FROM EXPERIENCE.
ANY SUGGESTTIONS CONTACT ME AT: k.j.hirner.wisdom@gmail.com ( with the header "Income.py and average-guess.sh SUGGESTIONS"

EOF

}

if [ ! -z "$1" ] ; then
 algo "$1"
else
 helper
fi

