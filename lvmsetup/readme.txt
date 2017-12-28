sqlite3-conf.sh will generate a configuuration entry with a rowid as the first column so that previous configurations can be used if necessary.

lvmset.sh should check for the db file first, if it exists, read the db for cofiguration options, using the last rowid available, if it does not exist, use the textfile configuration file , and if it does not exists as well, then use hardcoded options in lvmset.sh script.

in lvmset.sh, check to see if cmd arg 2 exists, and if it does, use the value to select the rowid for configuration, which cmd arg 2 must be checked to see if it is a valid integer, and that if it does exist in the database file.

make-host_db.sh -- creates a db that contains hostnames, ssh users,and vdisk paths for lvmset.sh createLVM
host.db -- see the above

sqlite3-conf.sh -- create the db configuration for lvmset.sh
lvmset.sh -- perform various automated lvm related operations
