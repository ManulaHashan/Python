import  mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb"
)
mycursor = mydb.cursor()

#sql = "UPDATE students SET age = 27 WHERE name = 'manula' "
#mycursor.execute(sql)
#mydb.commit()
#mycursor.execute("SELECT*FROM Students LIMIT 5 ")
mycursor.execute("SELECT*FROM Students LIMIT 5 OFFSET 2 ")
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
