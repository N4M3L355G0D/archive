#! /usr/bin/env python3
import os,gzip,base64,argparse
import xml.etree.ElementTree as ET

class resume:
    xmlFile="resume.xml"

    def dataContainerDump(self):
        data="""H4sIADi4ZloAA51Zy3bbOBJdu78CpzftnMiC49hxco7GZxQ5fqStSG3KTmYJkZCENkUwAGhFvep/
        mNX8Xn/J3AJAivJjJulFOxSJR+HWrVtV6J6RtlrKk592eqkunEgdHnd6hcC7gTA5+6itLBfsQplC
        GnZ5ednj/iONkkuhclZUy3/8/Ornk7vu792FH9ZdKZvp5T/n9L2b6mWP+6F+UrnQhWwmvd0/3Ht7
        dLh3uH903OP+G9nCN8b07J3Kc3syNnoMY2XhYMcRVppIsWS3Sq6k4UlywcvKuTV3Mi+kw+dbZVwl
        cvWHcEoXbCLTRaFzPVfSst3b4WdhZCeOea+/ddhvclnxX2+HLzD3fKGtYwNhaaHPCtsuhLmjD59u
        2PlgwM9fvmQDvSxVLg1eX6mi+sbGIr0Tc8mWosA/S1jK7No6ucSGrF+6DrseDzs0DCM67F9YntFu
        Q5UaneiZY6PZTKWSX6mpkfEHrd4fjvlVfzxmCTC5s3iVfM2Vk6/xdFlYJ/KciSJjw83GesZuhVG6
        siyR5l6aYINIF7LDPp0lHQbI6iexnIoOO5uM8ez/nl4M8Hfioeyw20+DDtY2SmRTmA9o5kYmv11h
        xPnktMOkS+kYKhkkl2SbP3PGb0pYZgjBpD/G34GyqWZqlJDV5URMc0lHIdSkYxMjUo/l4OVLPuAX
        k+EVH1+M+SBJ+HthF3y8dmDH7kH3eO919/gF76/ueHKBCaNSGvi4mLOwM1MBkuB3wqXlkF3mfcXP
        jJTvk1P+WRWZXtkXjRPjGpsp+PJJupU2dyDENMc+eHMtl9rJevCwPTiuGGFnB/v7b/nB/quDNgJs
        cEVIlbNEFlbCKGFZKkqn7iUrtYH1HWZ0BabDRf1Jh83AwRXO1GHOCOIFAyNxbk+fNXzB8R8xgm/c
        UzPLErNqq3ZruwiXU2nvnC4DCUXKRskX3i/LXEYv3UyrwlX8VE6VKPivCCY6BME4SviZzLQR/Fpm
        7ELQwceDgC19BCKZUfcCDwg4EbxUJJUlPvdNuqARvwujw5QGm8tR0uMx4EmSpHHWqwY9NaKBF1Gi
        ztQUZxkBuZTFSMDvAQarmYJlux8m/RcbxdrpZcLJk6FYs+MOXPPqqMf9m/BN2vTkVN7LXJeY6xaS
        3RV6lcsMQU14BcPYTBsWNtZ+4zbfLKbBc/MFS3VlLLSmNPpeZVhvumYfBuNLdlMoikfl1tictqTz
        cTpgUL545h5R7ss4Cm2Z6zU2fIzAQBQaYgJ1zKrUM54cDOEAA6uSyPTo+B+rfM3e+fMfM6fZKHWa
        TnPwJrxrY+KUy+XJqbLCWrlEyIKR1zLNhVpK0+Ph8wY9eto5lXtTMfeIVcXeVH/DJpQ84P0MNDfO
        KCAKHI2mYJ3qCiOdqYK07ex8KGwF/aMUAHKQhJWb0yEAJXD3IY+fG7TJCSR8U4vzh48QQXLiw9kY
        6KTfqVbsYF/bNLjYLlTpNQMQeZRZmiv8DkZeZnhUszV7bTJWYua6PR++vh5B609Ntex4JJqPfvaV
        mMqg2ZmyeD9FrJOtS9oM/yoEaAm7S4iuI4sRanPZqWeU2oqcTUG8APjGPW0jBJFRrhky3YaFHjPJ
        NlPWHhTvwhYda8Y9Qb+DNv0orf4B9B6RrCGV59QbOteZnJpKmDVePEe0ywlLSpkqSI11z9DrfaXy
        zCPRz5aqIPwII13sIaZk1KCY9PwETFVzxMiUJgYMFU4UEkIhVyzFg6FSAfjAgstiZpCbQUgHHgZv
        hxDvxHSiUJworFjvWavrVHiKozAg7a6zf9cvMYyz2ChO8mmX1bllhlJij8oMGUdTSqGQARNSRLMl
        BOOK9AZBE5kYFYtRlgwGhlTJbGpU6fxEnBcE8BSr15CURsDndB1CIRAk1EkqBb0opKrcxTjTFDaz
        WSRzBUYua3zrqUU8iti4JU6VIaL97jKtDLSPghP2Ob+VKhBwSz98a8WVnHqosnDEmGG/l6iv20S9
        fHPILpCz88dyKArPyqMNUx+Q9zFPBxGbAuURGON9KwtRpAHArn/r6dl9hsVPcte2WIvE6nlLK6kt
        RrKVcgsP5rmEbgG/wBbzi2XnlcrIjC3K8bpIDElWfq1Ug+XOTTk3IpO8GXyq0yrUkNGqukwYJb9E
        0a75fsy/jAmvUCjE0Ht11H21344aT5m4zdYRL7eisK5xmqLZH7P0JVKw1CmK0cau5hxerr3SVwbS
        KIlbDc9o85qZDzhfR04dg0mcw6n2QqHHY6gU4HqBnNfIQT3REwqYS1Ty9SJX2JCK0bGIWt/gGUY3
        UUIFhV8fqD4MgHoDL9MkJci5iF+wlEoOXWxHPqFnUW5Q0sfRDV4XlQyyA6beU+1UFT791r7cYAev
        a4RspmhdcGmrPq51tPsDYXe4VZ7o4quH5xqtm0Dh10FYCDiXjn+OXLV4KnN0m2D8689/U97ossPn
        QnFUuVBBoF1Bl2nQTDxZmUBnqHjHeTMFcUHbt6nVQpUgM5X6ErweCs0EaZHAbyUEwRDT5wJjoewV
        YFkzEw/V9l8XW/4AWkcP0IIgpI6qT80mCADfAvSzTELx2U3Sf6KWpf1jRj3yeH2sUOQcvHtc4AZM
        SKBGpWV9a5WvmZ5RqLE0dChfs/m+x4eZ51poIbbq3g5bLZRHIs0rLLLF81KvfH0VW75G4LPtXs2H
        rV8aeTBbUd3i2RlfGlFXiHWpn9FZFYpBlgAr9LYwY4KkR80xGyc3f/35Hxsy1n1shqP8PF63y3Yv
        qPOVEKAxmfsho4Ir9raNxbYdKjYU2Di5NJT+oNhZiDq6XVhgP5QjYqrNzo9x4k2bE496hgcESGQJ
        DfHZav/Va08A6m9qRjyVu2J5ci1LgUIzZny0eM8Qoc4MgLsWOdQGhaRgqRU21JdEkq1PVufVRq8a
        r6NV9FUYNZ2Nq6uQIeAw4w1rFVshtfo16J4kMmPDHF7P5QaN+b3It6qIrUKmThV1qxqEtKJyWmvX
        uJSGxZbYm9FkvJi4IO4P7ffpqp4D4b5jPmG5dThIaKwbHQ/C2l7tYhybcjBwe9FPsAim+1spP6Nx
        A0VUq7/hpiqKcEPxvVw73tIfo61FDr6jy60lQgsuHCyQWB6rdOBYJNzzQtNl/pruSorsuUKoypTm
        t3CU5jV6sXPlWxcrTWNIfRHMbzGDlGO7qvFDo4aXtfbUmmR9SwSstmgC5VVFW+buQV7sQHIRujK2
        OdF2SS+gcAhOyh3CLbUtSRB+wAlv2064VWYOQwQ71VQiwvFej57zwCHbY/1qjorc/3qip6Ib04IP
        9N6ofMYHTVCdbgptBBijW7hw0uYiqbmVBMY54tzovSFQEaFnuJY5rBpux+x3gvDu74Dg7zI8D9so
        vP5bKNBpD5mtsWg1HfVdxKZAGybot5Bx2Bn6Npb4TisGXkvmjNwToLejkkzJleWpNkamG0VsSWt9
        EfIcqmHCAG3qlHqGjDWFzxMzjJ/xv6q2Hm/ul3oS8hHUsXW/9H+yT4A/QN7ZVgK2O5a+Bn6xcQNg
        nqOkPHlPN9C5Nr7mrS2HzZZ9KOBwBBvmkcl+NJnZGHfyU4/X/7fivwXrHFe3GAAA"""
        
        file=open(self.xmlFile,'wb')
        xmlData=gzip.decompress(base64.b64decode(data.encode()))
        file.write(xmlData)
        file.close()

    def rootSet(self):
        if not os.path.exists(self.xmlFile):
            self.dataContainerDump()
        tree=ET.parse(self.xmlFile)
        root=tree.getroot()
        return root

    def banner(self,header=''):
        return '-'*len(header)*2+'\n'+' '*int(len(header)/2)+header+'\n'+'-'*len(header)*2
    
    def education(self,i):
        print(self.banner("Education"))
        for x in i:
            data=x.text.replace("\t","")
            if x.tag == "degree":
                print("\t\t- "+data)
            else:
                print("\t",x.text)
    
    def workXP(self,i):
        print(self.banner("Work Experience"))
        for x in i:
            data=x.text.replace("\t","") 
            for z in x:
                dataZ=z.text.replace("\t","")
                if z.tag == "desc":
                    desc=[d for d in dataZ.split("\n")]
                    for j in desc:
                        print("\t\t- "+j)
                else:
                    print("\t"+dataZ)

    def contact(self,i):
        print(self.banner(i.tag))
        for x in i:
            data=x.text.replace("\t","")
            if x.tag == "phone":
                print("\tPhone:",data)
            elif x.tag == "name":
                print("\tName:",data)
            elif x.tag == "email":
                print("\tEmail:",data)
    def skills(self,i):
        print(self.banner(i.tag))
        skills=[x for x in i.text.replace("\t","").split("\n")]
        for j in skills:
            print("\t- "+j)
    
    def certs(self,i):
        print(self.banner(i.tag))
        for x in i:
            for z in x:
                data=z.text.replace("\t","")
                if z.tag == "name":
                    print("\t"+data)
                elif z.tag == "date":
                    print("\t"+data)
                elif z.tag == "desc":
                    text=[d for d in data.split("\n")]
                    for j in text:
                        print("\t\t- "+j)

    def dataParse(self,root,section=None):
        for i in root:
            if i.tag =="education":
                if section == "education":
                    self.education(i)
                elif section == None:
                    self.education(i)
            elif i.tag == "workXP":
                if section == "workXP":
                    self.workXP(i) 
                elif section == None:
                    self.workXP(i)
            elif i.tag == "skills":
                if section == "skills":
                    self.skills(i)
                elif section == None:
                    self.skills(i)
            elif i.tag == "contact":
                if section == "contact":
                    self.contact(i)
                elif section == None:
                    self.contact(i)
            elif i.tag == "certs":
                if section == "certs":
                    self.certs(i)
                elif section == None:
                    self.certs(i)

    def cmdline(self):
        parser=argparse.ArgumentParser()
        parser.add_argument("-r","--resume",action="store_true")
        parser.add_argument("-s","--skills",action="store_true")
        parser.add_argument("-e","--education",action="store_true")
        parser.add_argument("-w","--workXP",action="store_true")
        parser.add_argument("-c","--certifications",action="store_true")
        parser.add_argument("-C","--contact",action="store_true")
    
        options=parser.parse_args()
        return options

    def main(self):
        root=self.rootSet()
        options=self.cmdline()
        noFail=[]

        if options.skills == False:
            noFail.append(False)
        if options.education == False:
            noFail.append(False)
        if options.workXP == False:
            noFail.append(False)
        if options.certifications == False:
            noFail.append(False)
        if options.contact == False:
            noFail.append(False)
        if options.resume == False:
            noFail.append(False)

        if len(noFail) < 6:
            if options.resume:
                self.dataParse(root)
            else:
                if options.skills:
                    self.dataParse(root,"skills")
                if options.education:
                    self.dataParse(root,"education")
                if options.workXP:
                    self.dataParse(root,"workXP")
                if options.certifications:
                    self.dataParse(root,"certs")
                if options.contact:
                    self.dataParse(root,"contact")
            os.remove(self.xmlFile)
        else:
            exit("please see -h/--help")
resumE=resume()
resumE.main()
#dataParse(root)


