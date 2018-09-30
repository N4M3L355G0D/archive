import pandas as pd
import csv,numpy

#get data from file
def loadDataRows(file='dataset1.txt'):
    rows=[]
    file='dataset1.txt'
    with open(file,'r') as idata:
        dataFile=csv.reader(idata,delimiter=',')
        for row in dataFile:
            rows.append(row)
    return rows

#display the rows from the file
def displayRowsFile(rows):
    for row in rows:
        print(row)

#separate the data
def loadSpecData(rows):
    freq={}
    genders=['male','female']
    statii=['admitted','rejected']
    for gender in genders:
        for status in statii:
            dat=[float(freq[3]) for num,freq in enumerate(rows) if num > 1 if freq[1].lower() == gender if freq[0].lower() == status]
            freq['-'.join((gender,status))]=numpy.array(dat,float)
    return freq

#basic processing of the data
def processData(freq,printVals=False):
    totals={}
    for key in freq.keys():
        vals={'mean':numpy.mean(freq[key]),'median':numpy.median(freq[key]),'std-dev':numpy.std(freq[key])}
        totals[key]=vals
        if printVals == True:
            for val in vals.keys():
                print(key,val,vals[val])
    return totals

def displayTotals(totals):
    for total in totals.keys():
        print(total,totals[total])

def sepo(target,totals):
    return numpy.array([totals[target][val] for val in totals[target].keys() ],float)

def dotProduct(ar1,ar2):
    result=numpy.dot(ar1,ar2)
    return result

rows=loadDataRows()
#displayRowsFile(rows)
freq=loadSpecData(rows)
totals=processData(freq)
#displayTotals(totals)

fa=sepo('female-admitted',totals)
ma=sepo('male-admitted',totals)

admittedDot=dotProduct(ma,fa)
#print(admittedDot)

def mkDataSeries(targets):
    series={}
    for target in targets:
        series[target]=pd.Series([i for i in totals[target].values()],index=[i for i in totals[target].keys()])
    return series

def mkDataSeries2(freq):
    result={}
    for target in freq.keys():
        data=freq[target]
        result[target]=pd.Series([target],index=data)
    return result

def mkDataFrame(seriesDict):
    return pd.DataFrame(seriesDict)


seriesD0=mkDataSeries(totals.keys())
seriesD1=mkDataSeries2(freq)

df0=mkDataFrame(seriesD0)

df1=mkDataFrame(seriesD1)
df1=df1.fillna('')
#print the first three rows
'''print(df.head(3))'''
#print the last three rows
'''print(df.tail(3))'''
#print the dtypes of each row
'''print(df.dtypes)'''
#print useful statistics
'''print(df.describe())'''
print(df0)
print(df1)

