import mysql.connector
import pandas as pd
# from xlsxwriter import Workbook

db1=[]
db2=[]
# wb = Workbook()
# ws = wb.active
def connection():

    db = mysql.connector.connect(host="127.0.0.1",
                                database='Work',
                                user="root",
                                password="admin")

    cursor = db.cursor()

    sql = " select * from db1 "
    sql1= "INSERT INTO db2 (id,username) VALUES (%s,%s)"
    sql2="select * from db2"


    try:
        cursor.execute(sql)
        for row in cursor:
            db1.append(row)
        
        for row in db1:
            val=(row[0],row[1])
            cursor.execute(sql1,val)
            db.commit()
            
        cursor.execute(sql2)
        for row in cursor:
            db2.append(row)


        cursor.close()
        db.close()

    except mysql.connector.ProgrammingError as err:
        print(err.errno)
        print(err.sqlstate)
        print(err.msg)

    except mysql.connector.Error as err:
        print(err)

connection()

# print(db1)
# print(db2)
db3=[]
for i in range(len(db1)):
    db3.append([db1[i][1],db2[i][1]])
# print(db3)

df1 = pd.DataFrame(db3,columns=['name','user'])
df1.to_excel("output.xlsx")