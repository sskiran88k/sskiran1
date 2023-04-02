import mysql.connector

db = mysql.connector.connect(
    host="192.168.209.161",
    user="kiran",
    password="1234"

)

cursor = db.cursor()
sql = """CREATE TABLE customers(
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255)
)
"""
cursor.execute(sql)

print("Table Created Successful !!!")
