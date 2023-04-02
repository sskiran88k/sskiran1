import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="192.168.209.161",
  user="kiran",
  password="1234"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute('create table sravani2.ssk(studentid int, firstname varchar(50), lastname varchar(50), registrationdate DATE, class varchar(20), course_name varchar(30))')
