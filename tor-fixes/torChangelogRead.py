#! /usr/bin/python3

installed_version=None
class dummy:
    Common=None
    class Common:
        paths={}
        def __init__(self):
            self.paths['tbb']={}
            self.paths['tbb']['changelog']='.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/TorBrowser/Docs/ChangeLog.txt'
    def __init__(self):
        self.common=self.Common()
        self.min_version='7.5.4'

def check_min_version(self):
    installed_version=None
    cl=self.common.paths['tbb']['changelog']
    for line in open(cl,'rb').readlines():
        if line.startswith(b'Tor Browser '):
            installed_version=line.split()[2].decode()
            break
    if self.min_version <= installed_version:
        return True

    return False

self=dummy()
print(check_min_version(self))
