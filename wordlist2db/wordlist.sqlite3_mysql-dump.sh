#! /usr/bin/env bash

sqlite3 wordlist.db .dump > spl.sql

sed -e '/PRAGMA/d' -e's/BEGIN/START/' -e 's/"wordlist"/wordlist/' < spl.sql | sed s\|"'"\|"\""\|g | sed s\|"\`"\|"\""\|g | sed s\|'CREATE TABLE IF NOT EXISTS "wordlist" ( WORD text, ID real );'\|'CREATE TABLE IF NOT EXISTS wordlist ( WORD text, ID real );'\|g | mysql -ucarl -pavalon wordlist

rm spl.sql
