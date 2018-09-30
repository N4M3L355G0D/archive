DESIRED_SIZE="2G"
# |& means to pipe all output, including stderr
#grep -v means to print everything except what is being grepped for
#since find displays errors with 'find: ' grep that out as well
#use awk to print the 11th column of the output to capture the text with appropriate slashes where needed

findBig(){
	find / -size +$DESIRED_SIZE  |& grep -v '.*\.iso$' | grep -v wordlists-ultimate.squashfs | grep -v 'find: ' | nl
}
findBig
