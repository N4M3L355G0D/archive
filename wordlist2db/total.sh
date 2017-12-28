#! /bin/bash
# take output of filter.sh and run it through sed to make a script which then is sent straight into bash
# up 12 hours for this shit
# and only just find the bug
bash filter.sh | sed s\|"^"\|"ls -lh "\|g | bash | less
