check to see if a path is in $PATH, as well as to list all user available paths. designed to be used in installation scripts 
as a way to avoid lengthy bash script writing to determine the existance of a path.

$PATH is what is on your system
$path_to_check is the path required for proper software operation and is compared against $PATH

useage:
/usr/bin/python3 pathcheck.py -p $path_to_check
