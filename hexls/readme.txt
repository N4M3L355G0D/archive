hexls.py <namefile> <path> -- python3 script to perform hexname dir listing
hexls2.py <namefile> <path> -- python2 script to perform hexname dir listing

to list or access non-ascii encoded filenames use the below method with the hexadecimal listing:
    filename prodide: `a2b699b4`.txt
        the within the backticks is the hexadecimal filename representation provided by hexls.py

        the command in bash to list it is as below:
            ls ''$'\xa2\xb6\x99\xb4''.t'
