import mysql.connector
#Встановлюємо зєднання з базою данних
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Nbvj[f16042007',
    database='my_first_db'
)
# Створюємо курсор
mycursor=mydb.cursor()

mycursor.execute('CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY,' 'name VARCHAR(255), salary INT(6))')
mydb.commit()
