#! /bin/awk -f

BEGIN {
 FS="|";
 OFS="|";
 counter=0;
}
{
 print;
 if ( $0 ~ /=/ ) {
  ignore=1;
  }
 else {
  if ( $0 !~ "\n" ) {
   if (( length(NR) > 0 )) {
    counter=counter+$2
   }
  }
 }
}
END {
 print "\n\nTotal Sales: " counter;
}
