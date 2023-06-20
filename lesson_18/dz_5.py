import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Nbvj[f16042007',
    database='my_first_db'
)
mycursor = mydb.cursor()

stud_data = 'INSERT INTO student (id, name) VALUES (%s, %s)'
val = ('01', 'John')
mycursor.execute(stud_data, val)

mycursor_1 = mydb.cursor()

emp_data = 'INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)'
val_1 = ('01', 'John', '10000')
mycursor_1.execute(emp_data, val_1)

mydb.commit()

