import MySQLdb

db = MySQLdb.connect(host="localhost", user="phpmyadmin", passwd="1122", db="mqtt_db")
cursor = db.cursor()

cursor.execute("SELECT * FROM iot_test")

results = cursor.fetchall()

for device_data in results:
	channel  = device_data[0]
	sf       = device_data[1]
	time     = device_data[2]
	gwip     = device_data[3]
	gwid     = device_data[4]
	repeater = device_data[5]
	systype  = device_data[6]
	rssi     = device_data[7]
	snr      = device_data[8]
	snr_max  = device_data[9]
	snr_min  = device_data[10]
	macAddr  = device_data[11]
	data     = device_data[12]
	frameCnt = device_data[13]
	fport    = device_data[14]
	print("%d, %d, %s, %s, %s, %s, %d, %f, %f, %f, %f, %d, %s, %d, %d" % (channel, sf, time, gwip, gwid, repeater,systype,rssi,snr,snr_max,snr_min,macAddr,data,frameCnt,fport))

db.close()

