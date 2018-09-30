#! /usr/bin/env bash
#noguilinux
#create configuration for deploy and kill
conf_db="conf.db"

read -rp "number of workers: " UP
read -rp "deployed workers pid db: " DB
read -rp "destination address to attack: " DST

sqlite3 $conf_db "create table if not exists conf (version INTEGER PRIMARY KEY AUTOINCREMENT,UP int, DB text, DST text);"
sqlite3 $conf_db 'insert into conf (UP,DB,DST) values ('"$UP"',"'"$DB"'","'"$DST"'");'
