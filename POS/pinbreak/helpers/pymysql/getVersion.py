import pymysql

def getVersion(hostname,user,password,database):
 #open database connection
 db = pymysql.connect(hostname,user,password,database)
 ##prepare a cursor object  using cursor() method
 cursor = db.cursor()
 # execute sql query using execute() method
 cursor.execute("SELECT VERSION()") 
 #fetch single row using fetchone() method
 data = cursor.fetchone()
 print("Database Version : %s" % data)
 #disconnect from server
 db.close()


getVersion("productlookup.net","store","avalon","cellular")
