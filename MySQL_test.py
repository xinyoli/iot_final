
import MySQLdb

db = MySQLdb.connect(host="localhost", user="phpmyadmin", passwd="1122", db="test_db")
cursor = db.cursor()

cursor.execute("SELECT * FROM products")

results = cursor.fetchall()

for record in results:
  col1 = record[0]
  col2 = record[1]
  print("%s, %s" % (col1, col2))

db.close()

