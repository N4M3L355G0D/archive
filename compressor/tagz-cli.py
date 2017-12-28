#! /usr/bin/python3

import argparse, tagz,sys, os

parser=argparse.ArgumentParser()
parser.add_argument("-c","--create",help="archive and compress input data",action="store_true")
parser.add_argument("-l","--list",help="list archive members",action="store_true")
parser.add_argument("-E","--extract-all",help="extract entire archive",action="store_true")
parser.add_argument("-e","--extract-member",help="extracts member(s) from archive")
parser.add_argument("-i","--input-data",help="file or directory to be archived and compressed",required="yes")
parser.add_argument("-o","--output-file",help="output filename, no extension necessary")
parser.add_argument("-d","--member-list-delimiter",help="member list separator in the event a comma cannot be used to separate members to extracted")
options=parser.parse_args()

if options.member_list_delimiter:
    member_delim=options.member_list_delimiter
else:
    member_delim=","

if options.create:
    tool=tagz.tagz()
    try:
        tool.idf=options.input_data
        if os.path.exists(options.input_data):
            if options.output_file:
                tool.ofile=options.output_file
            tool.archComp()
        elif not os.path.exists(options.input_data):
            print("That file/directory does not exist! Nothing will be done!")
    except:
        e = sys.exc_info()[0]
        write_to_page("<p>Error: %s<p>" % e )
else:
    try:
        tool=tagz.readArch()
        tool.infile=options.input_data
        if os.path.exists(options.input_data):
            if options.list:
                tool.operation="list"
                tool.read()
            elif options.extract_all:
                tool.operation="extract-all"
                tool.read()
            elif options.extract_member:
                tool.operation="extract-member"
                tool.member=options.extract_member.split(member_delim)
                tool.read()
        elif not os.path.exists(options.input_data):
            print("That file does not exist!")
    except:
        e = sys.exc_info()[0]
        write_to_page("<p>Error: %s<p>" % e )

