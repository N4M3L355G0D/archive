#! /usr/bin/awk -f

BEGIN { print "IPv$X\tAddr" }
{
 print $1,$2;
}
