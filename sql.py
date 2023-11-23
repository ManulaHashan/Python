import  mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb"
)
mycursor = mydb.cursor()

mycursor.execute("select * from students")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)