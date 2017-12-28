import os,shutil,time

failpoints="!@#$%^&*(){}[]\\|\";:'<>,?~` "

def walkit(dirs):
 pdf=""
 dest="/home/carl/Desktop/pdf/"
 for folder,f,io in os.walk(dirs):
  if len(io) > 0:
   for i in io:
    pdf=folder+"/"+i
    filename, file_ext = os.path.splitext(pdf)
    if file_ext == ".pdf":
     if os.path.exists(dest+i):
      shutil.copy(pdf,dest+str(time.ctime)+i)
      print(dest+str(time.ctime())+i)
     else:
      shutil.copy(pdf,dest)
      print(i)


walkit("/srv")
walkit("/home/carl")
