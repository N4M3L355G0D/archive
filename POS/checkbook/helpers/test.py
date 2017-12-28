import entryCheck,pymysql
sql2 = "SELECT * FROM TRACKING WHERE ( PHONE_NUMBER = '8043841879' and ORDER_NUMBER ='6442984' and "+"USER = 'carl' and "+"PLAN = '29.95' and PIN = '18159333277886' and BILL_DATE = '2-5-2017' and ACTIVATION = '0');"

a=entryCheck.readEntry("techzone.org","store","avalon","cellular",sql2)
print(a)

