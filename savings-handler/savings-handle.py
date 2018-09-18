#! /usr/bin/env python3

import os,time,argparse,sys,json

class colors:
    red='\033[1;31;40m'
    green='\033[1;32;40m'
    yellow='\033[1;33;40m'
    blue='\033[1;34;40m'
    cyan='\033[1;35;40m'
    lightblue='\033[1;36;40m'
    reset='\033[1;40;m'
    
class app: 
    new='''{
        "#SECOND#:#MINUTE#:#HOUR#_#MONTH#.#DAY#.#YEAR#":{
		"date":{
			"month":#MONTHINT#,
			"day":#DAYINT#,
			"year":#YEAR#
		},
		"saved_expanded":{
			"100bills":0,
			"50bills":0,
			"20bills":0,
			"10bills":0,
			"5bills":0,
			"1bills":0,
			"quarters":0,
			"nickels":0,
			"dimes":0,
			"pennies":0
		},
		"saved_converted":{
			"100bills":0,
			"50bills":0,
			"20bills":0,
			"10bills":0,
			"5bills":0,
			"1bills":0,
			"quarters":0,
			"nickels":0,
			"dimes":0,
			"pennies":0
		},
		"saved_condensed":{
			"total":0
		}
	}
}'''
    currency={
        'quarters':0.25,
        'nickels':0.05,
        'dimes':0.1,
        'pennies':0.01,
        '100bills':100,
        '50bills':50,
        '20bills':20,
        '10bills':10,
        '5bills':5,
        '1bills':1,
        }
    failedStates=[None,{},[],'']
    def __init__(self):
        self.colors=colors()
        lt=time.localtime()
        if len(str(lt.tm_mday)) < 2:
            day='0{}'.format(lt.tm_mday)
        else:
            day=lt.tm_mday

        if len(str(lt.tm_mon)) < 2:
            mon='0{}'.format(lt.tm_mon)
        else:
            mon=lt.tm_mon
        if len(str(lt.tm_hour)) < 2:
            hour='0{}'.format(lt.tm_hour)
        else:
            hour=str(lt.tm_hour)

        if len(str(lt.tm_min)) < 2:
            minute='0{}'.format(lt.tm_min)
        else:
            minute=str(lt.tm_min)

        if len(str(lt.tm_sec)) < 2:
            second='0{}'.format(lt.tm_sec)
        else:
            second=str(lt.tm_sec)

        replaces=[
            ('#MONTH#',str(mon)),
            ('#MONTHINT#',str(lt.tm_mon)),
            ('#DAY#',str(day)),
            ('#DAYINT#',str(lt.tm_mday)),
            ('#YEAR#',str(lt.tm_year)),
            ('#HOUR#',hour),
            ('#MINUTE#',minute),
            ('#SECOND#',second),
                ]
        for i,x in replaces:
            self.new=self.new.replace(i,x)
        
    def jsonLoad(self,fname=None,fileOrNew='file'):
        data=None
        if fileOrNew == 'file':
            with open(fname,'r') as ifile:
                data=json.load(ifile)
        elif fileOrNew == 'new':
            data=json.loads(self.new)
        else:
            data=json.loads(self.new)
        return data

    def breakDate(self,key,month,day,year):
        return '{4}{3}{5}\n{6}[{7}] {0}/{1}/{2}{5}\n{4}{3}{5}'.format(
                month,
                day,
                year,
                '='*20,
                self.colors.lightblue,
                self.colors.reset,
                self.colors.cyan,
                key)

    def print_contents(self,value=None,data=None):
        if value in self.failedStates:
            if data not in self.failedStates:
                for key in data.keys():
                    d=data[key]
                    print(self.breakDate(key,d['date']['month'],d['date']['day'],d['date']['year']))
                    for skey in d.keys():
                        sub_d=d[skey]
                        for sskey in sub_d.keys():
                            sub_sd=sub_d[sskey]
                            print('{3}{0}{5} : {6}{1}{5} : {4}{2}{5}'.format(
                                skey,
                                sskey,
                                sub_sd,
                                self.colors.red,
                                self.colors.green,
                                self.colors.reset,
                                self.colors.yellow))

    def lastRealEntry(self,data={}):
        dk=[]
        if data not in self.failedStates:
            for key in data.keys():
                tkey=time.strptime(key,'%S:%M:%H_%m.%d.%Y')
                dk.append(time.mktime(tkey))
        keys=sorted(dk)
        keys=[time.strftime('%S:%M:%H_%m.%d.%Y',time.localtime(k)) for k in keys]
        return keys[-1]

    def mkNewEntry(self,data=None,keys={}):
        localtime=time.localtime()
        date={}
        date['day']=localtime.tm_mday
        date['month']=localtime.tm_mon
        date['year']=localtime.tm_year
        keyname=time.strftime('%S:%M:%H_%m.%d.%Y',localtime)
        ldata=None
        if data not in self.failedStates:
            if keys not in self.failedStates:
                ldata=data[self.lastRealEntry(data)]
                #print(keyname,ldata)
                for key in keys.keys():
                    if key in ldata['saved_expanded'].keys():
                        ldata['saved_expanded'][key]+=keys[key]
                        ldata['saved_converted'][key]+=keys[key]*self.currency[key]
                        ldata['saved_converted'][key]=round(ldata['saved_converted'][key],2)
                        total=0
                        for skey in ldata['saved_converted'].keys():
                            total+=ldata['saved_converted'][skey]
                        ldata['saved_condensed']['total']=round(total,2)
                        ldata['date']=date
        return ldata,keyname

    def writeContents(self,data,ifile):
        with open(ifile,'w') as odata:
            json.dump(data,odata)

    def report(self,data):
        d={}
        d[self.lastRealEntry(data)]=data[self.lastRealEntry(data)]
        self.print_contents(data=d)


class utility:
    args={
            'report':{
                'args':{
                    'report latest':{'short':'-l','long':'--report-latest','help':'print the latest entry'},
                    'report all':{'short':'-a','long':'--report-all','help':'print all entries'},
                }
            },
            'add entry':{'args':{
                'file':{'short':'-f','long':'--log-file','help':'file where savings is tracked','required':'yes'},
                    'pennies':{'short':'-p','long':'--pennies','help':'number of pennies'},
                    'quarters':{'short':'-q','long':'--quarters','help':'number of quarters'},
                    'nickels':{'short':'-n','long':'--nickels','help':'number of nickels'},
                    'dimes':{'short':'-d','long':'--dimes','help':'number of dimes'},
                    '100bills':{'short':'-100','long':'--100bills','help':'number of 100bills'},
                    '50bills':{'short':'-50','long':'--50bills','help':'number of 50bills'},
                    '20bills':{'short':'-20','long':'--20bills','help':'number of 20bills'},
                    '10bills':{'short':'-10','long':'--10bills','help':'number of 10bills'},
                    '5bills':{'short':'-5','long':'--5bills','help':'number of 5bills'},
                    '1bills':{'short':'-1','long':'--1bills','help':'number of 1bills'},
                    'dry_run':{'short':'-D','long':'--dry-run','help':'do not write data to log file; print to screen','action':'store_true'},
                },
                
            },
            'init':{'args':{
                'file':{'short':'-f','long':'--log-file','help':'file to make','required':'yes'},
                },
            },
        }
    def __init__(self):
        self.logging=app()
        
    def reportOne(self,args):
        fname=args.report_latest
        if fname != None:
            j=self.logging.jsonLoad(fname)
            self.logging.report(j)

    def reportAll(self,args):
        fname=args.report_all
        if fname != None:
            j=self.logging.jsonLoad(fname)
            self.logging.print_contents(data=j)

    def reportProxy(self,args):
        if args.report_latest != None:
            self.reportOne(args)
        elif args.report_all != None:
            self.reportAll(args)
        else: 
            self.reportOne(args)

    def initProxy(self,args):
        if args.log_file != None:
            new=self.logging.jsonLoad(fileOrNew='new')
            self.logging.writeContents(new,args.log_file)

    def addEntryProxy(self,args):
        self.addEntry(args)

    def addEntry(self,args):
        j=app()
        log=j.jsonLoad(args.log_file)
        attribs={attr:getattr(args,attr) for attr in dir(args) if not callable(getattr(args,attr)) and not attr.startswith('__') if attr not in ['log_file','dry_run']}
        for key in attribs.keys():
            if key != 'log_file':
                if attribs[key] == None:
                    attribs[key]=0
                if type(attribs[key]) == type(str()):
                    try:
                        attribs[key]=int(attribs[key])
                    except:
                        print(sys.exc_info())
        
        new=j.mkNewEntry(log,keys=attribs)
        e={new[-1]:new[0]}

        j.report(j.jsonLoad(args.log_file))
        j.print_contents(data=e)
        log[new[-1]]=new[0]

        if args.dry_run == False:
            j.writeContents(log,args.log_file)

    def cmdline(self):
        subs={}
        subsp=None
        parser=argparse.ArgumentParser()
        subsp=parser.add_subparsers()
        for arg in self.args.keys():    
            subs[arg]=subsp.add_parser(arg.replace(' ','-'))
            for sarg in self.args[arg]['args'].keys():
                if 'required' in self.args[arg]['args'][sarg].keys():
                    subs[arg].add_argument(self.args[arg]['args'][sarg]['short'],self.args[arg]['args'][sarg]['long'],help=self.args[arg]['args'][sarg]['help'],required=self.args[arg]['args'][sarg]['required'])
                elif 'action' in self.args[arg]['args'][sarg].keys():
                    subs[arg].add_argument(self.args[arg]['args'][sarg]['short'],self.args[arg]['args'][sarg]['long'],help=self.args[arg]['args'][sarg]['help'],action=self.args[arg]['args'][sarg]['action'])
                else:
                    subs[arg].add_argument(self.args[arg]['args'][sarg]['short'],self.args[arg]['args'][sarg]['long'],help=self.args[arg]['args'][sarg]['help'])
                
            if arg == 'report':
                subs[arg].set_defaults(func=self.reportProxy)
            if arg == 'add entry':
                subs[arg].set_defaults(func=self.addEntryProxy)
            if arg == 'init':
                subs[arg].set_defaults(func=self.initProxy)

        options=parser.parse_args()
        try: 
            options.func(options)
        except:   
            print(sys.exc_info())
            options=parser.parse_args('--help'.split())
        #print(options)
        return options

if __name__ == '__main__':
    u=utility()
    u.cmdline()
    '''
    #need to make cmdline utility class
    a=app()
    j=a.jsonLoad('savings-log.json',fileOrNew='file')
    #add new value to last entry stored in data file
    ##in this case add 20 quarters, and 10 100 dollar bills
    new=a.mkNewEntry(j,keys={'quarters':20,'100bills':10})
    #copy new entry into stored data
    j[new[1]]=new[0]
    #print data stored
    '''
    '''
    #report all
    a.print_contents(data=j)
    '''
    #save new data
    #a.writeContents(j,'savings-log.json')
    '''
    #report latest
    a.report(j)
    '''
