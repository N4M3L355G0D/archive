#! /usr/bin/env python3
#https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv

import pandas as pd,csv, numpy as nm


rows=[]
file='titanic-survivors.txt'
'''
with open(file,'r') as idata:
    data=csv.reader(idata,delimiter=',')
    for row in data:
        rows.append(row)
'''
rows=pd.read_csv(file)
df=pd.DataFrame(rows)
#df=df.fillna(df['Age'].mean())
predictions={}
survivors=0
for passenger_index,passenger in df.iterrows():
    if passenger['Sex'] == 'female' and passenger['Age'] <= 61 and passenger['Pclass'] == 1:
        predictions[passenger['PassengerId']]=1
    elif passenger['Sex'] == 'female' and passenger['Age'] <= 30 and passenger['Pclass'] == 2:
         predictions[passenger['PassengerId']]=1
    elif passenger['Sex'] == 'female' and passenger['Age'] <= 30 and passenger['Pclass'] == 3:
         predictions[passenger['PassengerId']]=1
    elif passenger['Sex'] == 'male' and passenger['Pclass'] == 2 and passenger['Age'] < 18:
         predictions[passenger['PassengerId']]=1
    elif passenger['Sex'] == 'male' and passenger['Pclass'] == 3 and passenger['Age'] < 14:
         predictions[passenger['PassengerId']]=1
    elif passenger['Sex'] == 'male' and passenger['Pclass'] == 1 and passenger['Age'] < 80:
         predictions[passenger['PassengerId']]=1

survivorDF=df[['Age','Sex','Pclass','Survived']][df['Survived'] == 1]
print(survivorDF)
print(predictions)
'''
if passenger['Sex'] == 'female' or ( passenger['Age'] <= 18 and passenger['Pclass'] <= 2) or passenger['Survived']:
    predictions[passenger['PassengerId']]=1
else:
    predictions[passenger['PassengerId']]=0
'''
