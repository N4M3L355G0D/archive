./sha512pass -e $PASS
./sha512pass -s $SALT -p $PASS -d

-create sha512 hash storage using random number generated from sodium's randombytes_uniform(date_value)

-reverse storage from password and salt provision

shAss -- name reasoning:
 sha[512] - [pain-in-the-]Ass

[NOTES]

 please note that this dumps the information to STDOUT, and nowhere else, at least for the moment.
