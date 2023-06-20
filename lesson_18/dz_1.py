import mysql.connector
#Встановлюємо зєднання з базою данних
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Nbvj[f16042007',
    database='pds_7'
)
# Створюємо курсор
mycursor=mydb.cursor()

mycursor.execute('CREATE DATABASE my_first_db')
