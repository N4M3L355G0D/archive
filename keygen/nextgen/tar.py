import tarfile, os, time

class tar():
    output=str()
    def __init__(self):
        self.output=self.date()+".tar.xz"
    Time=str()

    def date(self):
        for i in time.localtime():
            self.Time+=str(i)
        return self.Time
    source_dir="/srv/samba/build/archive/keygen"
    def make_tarfile(self,output,source_dir):
        with tarfile.open(output,"w:xz") as tar:
            tar.add(source_dir,arcname=os.path.basename(source_dir))
'''
a=tar()
a.make_tarfile(a.output,a.source_dir)
'''
