mysqldump --single-transaction --flush-logs --master-data=2 --all-databases -u root -p | gzip > $srv/db/all_databases`date +%D | sed s\|"\/"\|"_"\|g`.sql.gz
