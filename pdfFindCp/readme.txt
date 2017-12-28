if exists dir1:
 if dir1 directory:
  if file2 exists:
   a=hash file1
   b=hash file2
   if a == b:
    copy file1 file2
   if a != b:
    copy file1 file2.`date`
 if not dir1 directory:
  mv dir1 dir1.file.`date`
  print " moved dir1 to dir1.file.`date`
  mkdir dir1

operational syntax:
python3 pdfFindCp.py -d $DEST -s $SRC -e $EXTENSION
