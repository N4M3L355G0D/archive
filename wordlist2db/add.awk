#! /usr/bin/awk -f

BEGIN{
	acc=0;
	OFS="<+>";
}
{
	acc+=$1;
}
END{
	print acc;
}
