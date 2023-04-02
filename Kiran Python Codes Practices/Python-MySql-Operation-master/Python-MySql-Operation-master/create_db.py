import mysql.connector

db = mysql.connector.connect(
    host="192.168.209.161",
    user="kiran",
    password="1234"

)

cursor = db.cursor()
cursor.execute("CREATE DATABASE employee_data")

print("Database Created Successful !!!")
