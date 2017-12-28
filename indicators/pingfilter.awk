#! /usr/bin/awk -f

BEGIN {
	OFS=" ";
}
{
	if (( $0 !~ /PING/ ) && ( $0 !~ /ping/ ) && ( $0 !~ /packets/ ) && ( $0 !~ /rtt min/ ) && ($0 != ""))  {
	print $4,$5,$8;
	}
}
