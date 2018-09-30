check for required script dependencies

example:

if ./depCheck.sh "dependency_1 dependency_2" ; then
	do_action_if_deps_are_met
else
	#missing deps will be printed
	missing_deps_action
fi
