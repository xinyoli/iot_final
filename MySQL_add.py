import MySQLdb

db = MySQLdb.connect(host="140.114.14.225",
    user="phpmyadmin", passwd="1122",
    db="db_name", charset="utf8")
cursor = db.cursor()

# 插入資料
cursor.execute('INSERT INTO products (name, descr, price) '
        'VALUES ("葵花寶典", "蓋世武功密集", 990);')
db.commit()

db.close()