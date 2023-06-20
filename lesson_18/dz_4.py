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

mycursor.execute('ALTER TABLE student MODIFY id INT AUTO_INCREMENT PRIMARY KEY')

mydb.commit()


