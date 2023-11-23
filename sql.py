import  mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb"
)
mycursor = mydb.cursor()

sqlFormula = "INSERT INTO students(name,age) VALUES (%s, %s)"
students = [("Hashan", 28),
            ("Dhanu", 27),
            ("Kapila", 30),
            ("Maniya", 25),
            ("Kamal", 35),]
mycursor.executemany(sqlFormula, students)
mydb.commit()
