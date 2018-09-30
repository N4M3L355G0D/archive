DB="bcard.db"

if test -e "$DB" ; then
	rm "$DB"
fi

#bcard section
sqlite3 "$DB" "create table if not exists bcard(name text,email text,phone text,version INTEGER PRIMARY KEY AUTOINCREMENT)"
sqlite3 "$DB" "insert into bcard(name,email,phone) values ('Carl Joseph Hirner III','k.j.hirner.wisdom@gmail.com','804-854-4057');"


#summary of skills field
sqlite3 "$DB" "create table if not exists summaryOfSkills (subcat text,rowid INTEGER PRIMARY KEY AUTOINCREMENT);"

subcat=("software" "skills" "operatingSystems")
for i in ${subcat[@]} ; do
	sqlite3 "$DB" "insert into summaryOfSkills (subcat) values ('$i');"
	sqlite3 "$DB" "create table if not exists $i (element text,rowid INTEGER PRIMARY KEY AUTOINCREMENT);"
	input=''
	while test "$input" != ".quit" ; do
		read -rp "$i Element: " input
		if test "$input" != ".quit" ; then
			sqlite3 "$DB" "insert into $i (element) values (\"$input\");"
		fi
	done
done

#cert field
input=''
sqlite3 "$DB" "create table if not exists certifications ( cert text,date text,desc text, rowid INTEGER PRIMARY KEY AUTOINCREMENT);"
while test "$input" != ".quit" ; do
	read -rp "cert: " input
	if test "$input" != ".quit" ; then
		read -rp "desc: " desc
		if test "$desc" != ".quit" ; then
			read -rp "date: " DATE
			if test "$DATE" != ".quit" ; then
				sqlite3 "$DB" "insert into certifications (cert,date,desc) values (\"$input\",\"$DATE\",\"$desc\");"
			fi
		fi
	fi
done

#work experience field
input=''
sqlite3 "$DB" "create table if not exists workXP ( employer text,title text,date text,desc text, rowid INTEGER PRIMARY KEY AUTOINCREMENT);"
while test "$input" != ".quit" ; do
	read -rp "employer: " input
	if test "$input" != ".quit" ; then
		read -rp "title: " title
		if test "$title" != ".quit" ; then
			read -rp "date: " DATE
			if test "$DATE" != ".quit" ; then
				read -rp "desc: " desc
				if test "$desc" != ".quit" ; then
					sqlite3 "$DB" "insert into workXP (employer,title,date,desc) values (\"$input\",\"$title\",\"$DATE\",\"$desc\");"
				fi
			fi
		fi
	fi
done

#education field
input=''
sqlite3 "$DB" "create table if not exists education ( uni text,date text,degree text, rowid INTEGER PRIMARY KEY AUTOINCREMENT);"
while test "$input" != ".quit" ; do
	read -rp "uni: " input
	if test "$input" != ".quit" ; then
		read -rp "date: " DATE
		if test "$DATE" != ".quit" ; then
			read -rp "degree: " degree
			if test "$degree" != ".quit" ; then
				sqlite3 "$DB" "insert into education (uni,date,degree) values (\"$input\",\"$DATE\",\"$degree\");"
			fi
		fi
	fi
done
