import mysql.connector

mydb = mysql.connector.connect(
  host="sql12.freemysqlhosting.net",
  user="sql12322378",
  passwd="dBbRczdtnt",
  database="sql12322378"
)

mycursor = mydb.cursor()

mycursor.execute("select MENCode, S_Name from station")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)