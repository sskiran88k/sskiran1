import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("""insert into kiran.ssk values(434, 'SS Kiran', 'SSK', '2023-03-11','SQL', 'Data Science'), 
(435, 'Guru Charan', 'SSK', '2023-03-11','SQL', 'Data Science'), 
(436, 'Siva Nandini', 'SSK', '2023-03-11','SQL', 'Data Science'), 
(437, 'Roshini', 'SSK', '2023-03-11','SQL', 'Data Science'), 
(438, 'Gayatri', 'SSK', '2023-03-11','SQL', 'Data Science'), 
(439, 'Kavya', 'SSK', '2023-03-11','SQL', 'Data Science'), 
(440, 'Teju', 'SSK', '2023-03-11','SQL', 'Data Science')""")

mydb.commit()

mycursor.execute('select * from kiran.ssk')

for i in mycursor:
    print(i)
