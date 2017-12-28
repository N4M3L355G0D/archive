#! /usr/bin/env bash

echo -e "run this once for each host that will be added to your storage array in the order by which they will be mountedi!\n\n"

sqlite3 "hosts.db" "create table if not exists hosts ( rowid INTEGER PRIMARY KEY AUTOINCREMENT,user text, host text, diskpath );"
read -rp "user: " User
read -rp "host: " Host
read -rp "diskpath: " diskpath
sqlite3 "hosts.db" "insert into hosts (user,host,diskpath) values ('$User','$Host','$diskpath');"
