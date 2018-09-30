checkForNum() {
 python << EOF
import string
if '$1' != '':
 for i in '$1':
  if i not in string.digits:
   exit("invalid characters")
else:
 exit("invalid characters")
print('$1')

EOF
 
}
DBCNF="lvmsetup-conf.db"
table="cnf"
SQL="create table if not exists $table (rowid INTEGER PRIMARY KEY AUTOINCREMENT,VG text, LV text,DISKPATH_TOP text,DISKSIZE text,LVSIZE text, fname text, top_num text, bot_num text,id real);"
sqlite3 "$DBCNF" "$SQL"

read -rp "VG: " VG
read -rp "LV: " LV
read -rp "DISKPATH_TOP: " DISKPATH_TOP
read -rp "DISKSIZE: " DISKSIZE
read -rp "fname: " fname

checkRes="`checkForNum $DISKSIZE`"
if test "$checkRes" != "invalid characters" ; then
 read -rp "LVSIZE: " LVSIZE
 checkRes="`checkForNum $LVSIZE`"
 if test "$checkRes" != "invalid characters" ; then
  read -rp "top_num: " top_num
  checkRes="`checkForNum $top_num`"
  if test "$checkRes" != "invalid characters" ; then
   read -rp "bot_num: " bot_num
   checkRes="`checkForNum $bot_num`"
   if test "$checkRes" != "invalid characters" ; then
    if test ! "`expr $bot_num \* $DISKSIZE`" -le "$LVSIZE" ; then
     SQL="insert into $table (VG,LV,DISKPATH_TOP,DISKSIZE,LVSIZE,fname,top_num,bot_num) values ('""$VG""','""$LV""','""$DISKPATH_TOP""','""$DISKSIZE""','""$LVSIZE""','""$fname""','""$top_num""','""$bot_num""');"
     echo $SQL
     sqlite3 "$DBCNF" "$SQL"
    else
     echo "LVSIZE is greater than, or equal to, the storage available"
    fi
   else
    echo "bot_num is not a valid number"
   fi
  else
   echo "top_num is not a valid number"
  fi
 else
  echo "LVSIZE is not a valid number ( is it in bytes? )"
 fi
else
 echo "DISKSIZE is not a valid number ( is it in bytes? )"
fi
