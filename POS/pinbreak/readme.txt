a cellular sales POS system, utilizing a MariaDB Server, python, awk, and bash.

you will need to have a mysql server installed, and the pinbreak.cfg must have the location ( ipaddress or url ), for pinbreak to operate properly.

to install this program, use the below commands, keeping in mind that you must have a mysql server, mariadb in this case, for pinbreak to operate correctly, if at all.

sudo bash install.sh

you need to be in the ../pinbreak directory, or i should say, since you are reading this, you must already be there. More updates will be provided soon. if you have any suggestions, please let me know at k.j.hirner.wisdom@gmail.com .

changes as of this version
	removed pinger.sh call in indicator
		code will remain for now
			will be removed later

current version, as of 3-6-2017 

	run `bash install.sh`
	once installation is complete
        please note that the following step will erase any tables that have the same db, and table name. back them up before running the below script.
	edit pinbreak.cfg in the root of the pinbreak directory for your sql servers requirements
	run `python3 helpers/createTable.py`
