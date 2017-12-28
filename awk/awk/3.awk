#! /usr/bin/awk -f

BEGIN { print "type a 2 space delimited numbers" } 
{
 i=$1;
 while ( i <= $2 ) {
  print i*i," ";
  i++;
 }
 print "\n"
 for ( i=$1 ; i <= $2; i++){
  print i*i," ";
 }
 exit;
}
END { print "\nDONE" }
