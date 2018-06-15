import MySQLdb

db = MySQLdb.connect(host="localhost", user="phpmyadmin", passwd="1122", db="mqtt_db", charset="utf8")
cursor = db.cursor()

cursor.execute('INSERT INTO iot_test (channel, sf, time, gwip, gwid, repeater,systype,rssi,snr,snr_max,snr_min,macAddr,data,frameCnt,fport) '
	'VALUES (923375000, 10, "2018-06-14T11:35:19", "140.114.71.156", "00001c497b431e9f", "00000000ffffffff", 18, -95.0, 18.0, 32.0, 12.0, 0000000012345611, "b000168",11,15);')
db.commit()

db.close()
