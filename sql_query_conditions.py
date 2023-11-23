import mysql.connector
mydb =  mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb"
)
mycursor = mydb.cursor()
#sql = "SELECT * FROM students WHERE name like'%m%' AND age = 27 "
#sql = "SELECT * FROM students WHERE name like'%m%' "
#sql = "SELECT * FROM students WHERE name ='manula' AND age = 27 "

sql = "SELECT * FROM students WHERE name = %s "
mycursor.execute(sql, ("Manula",))
myresult = mycursor.fetchall()
for result in myresult:
    print(result)