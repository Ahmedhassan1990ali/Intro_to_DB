import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    password = "mypass"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE alx_book_store")
    print ("Database 'alx_book_store' created successfully!")
except as E:
    print(E)



mycursor.close()
mydb.close()
