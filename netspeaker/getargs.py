#! /usr/bin/env python3
#this is the argument parser for netspeaker.sh
#NoGuiLinux
import argparse,os
try:
    import sqlite3
    def save(options,nsDb):
        try:
            db=sqlite3.connect(nsDb)
            cursor=db.cursor()
            #get rid of old settings
            sql="drop table if exists nsSettings;"
            cursor.execute(sql)
            try:
                sql="create table if not exists nsSettings (server text, clients text, port text, user text, rate text);"
                cursor.execute(sql)
            except OSError as err:
                print(err)
                exit(1)
            try:
                sql='insert into nsSettings (server,clients,port,user,rate) values ("'+options.server+'","'+options.clients+'","'+options.port+'","'+options.user+'","'+options.rate+'");'
                cursor.execute(sql)
                db.commit()
                db.close()
            except OSError as err:
                print(err)
                exit(1)

        except OSError as err:
            print(err)
            exit(1)

    def get_settings(nsDb):
        if os.path.exists(nsDb):
            if os.path.isfile(nsDb):        
                try:
                    db=sqlite3.connect(nsDb)
                    cursor=db.cursor()
                    sql="select * from nsSettings;"
                    cursor.execute(sql)
                    settings=cursor.fetchall()[0]
                    if settings != None:
                        db.close()
                        saved={'server':settings[0],"clients":settings[1],"port":settings[2],"user":settings[3],"rate":settings[4]}
                        return saved
                    else:
                        db.close()
                        exit("no settings were found")
                except OSError as err:
                    print(err)
                    exit(1)
            else:
                print("!File: {}".format(nsDb))
                exit(1)
        else:
            print("Does!Exist: {}".format(nsDb))
            exit(1)
    

except:
    error_sqlite3_import="something went wrong and sqlite3 could not be imported. This option is disable"
    def save(options,nsDb):
        print(error_sqlite3_import)
        exit(1)

    def get_settings(nsDb):
        print(error_sqlite3_import)
        exit(1)


def main():
    blank=[""," "]
    parser=argparse.ArgumentParser()
    parser.add_argument("-s","--server")
    parser.add_argument("-c","--clients")
    parser.add_argument("-p","--port")
    parser.add_argument("-u","--user")
    parser.add_argument("-r","--rate")
    parser.add_argument("-g","--save-to-db",action="store_true")
    parser.add_argument("-G","--use-db-options",action="store_true")
    parser.add_argument("-D","--setting-db-location")
    options=parser.parse_args()
    
    noopt="error_no_options"
    if options.setting_db_location:
        if os.path.exists(os.path.split(options.setting_db_location)[0]):
            nsDb=options.setting_db_location
        else:
            nsDb="ns-settings.db"

    if not options.use_db_options:
        if options.server:
            print("server: {}\n".format(options.server))
        else:
            print("server: {}\n".format(noopt))
        
        if options.clients:
            print("clients: {}\n".format(options.clients))
        else:
            print("clients: {}\n".format(noopt)) 
        if options.port:
            print("port: {}\n".format(options.port))
        else:
            print("port: {}\n".format(noopt))
        
        if options.user:
            print("user: {}\n".format(options.user))
        else:
            print("user: {}\n".format(noopt))
        
        if options.rate:
            print("rate: {}\n".format(options.rate))
        else:
            print("rate: {}\n".format(noopt))
    
        if options.save_to_db:
            save(options,nsDb)
    else:
        settings=get_settings(nsDb)
        for key in settings.keys():
            if settings[key] not in blank:
                print("{}: {}\n".format(key,settings[key]))
            else:
                print("{}: {}\n".format(key,noopt))
        
main()
