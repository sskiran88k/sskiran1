import mysql.connector

db = mysql.connector.connect(
    host="192.168.209.161",
    user="kiran",
    password="1234"
)

if db.is_connected():
    print("Database Connected")
