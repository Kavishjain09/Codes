import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="Kavish@0901", database="dbe")
mycursor = mydb.cursor()
mycursor.execute("select * from employee")


#(fetch all data)
for i in mycursor:
    print(i)

#(fetch only one data)
#result=mycursor.fetchone()
#print(result)
