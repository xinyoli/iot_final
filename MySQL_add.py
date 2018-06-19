import MySQLdb

# insert_stmt = (
	# "INSERT INTO iot_test (channel, sf, time, gwip, gwid, repeater,systype,rssi,snr,snr_max,snr_min,macAddr,data,frameCnt,fport)"
	# "VALUES (%(channel)d, %(sf)d, %(time)s, %(gwip)s, %(gwip)s, %(repeater)s, %(systype)d, %(rssi)f, %(snr)f, %(snr_max)f, %(snr_min)f, %(macAddr)s, %(data)s, %(frameCnt)d, %(fport)d)"
# )
# data = {
	# "channel" : 923375000, 
	# "sf" : 10, 
	# "time" : "2018-06-14T11:35:19", 
	# "gwip" : "140.114.71.156", 
	# "gwid" : "00001c497b431e9f", 
	# "repeater" : "00000000ffffffff", 
	# "systype" : 18, 
	# "rssi" : -95.0, 
	# "snr" : 18.0,
	# "snr_max" : 32.0, 
	# "snr_min" : 12.0, 
	# "macAddr" : "0000000012345611", 
	# "data" : "b000168", 
	# "frameCnt" : 11, 
	# "fport" : 15
# }

insert_stmt = (
	"INSERT INTO iot_test (channel, sf, time, gwip, gwid, repeater,systype,rssi,snr,snr_max,snr_min,macAddr,data,frameCnt,fport)"
	"VALUES (%(channel)s, %(sf)s, %(time)s, %(gwip)s, %(gwid)s, %(repeater)s, %(systype)s, %(rssi)s, %(snr)s, %(snr_max)s, %(snr_min)s, %(macAddr)s, %(data)s, %(frameCnt)s, %(fport)s)"
)
data = {
	"channel" : 923375000, 
	"sf" : 10, 
	"time" : "2018-06-14T11:35:19", 
	"gwip" : "140.114.71.156", 
	"gwid" : "00001c497b431e9f", 
	"repeater" : "00000000ffffffff", 
	"systype" : 18, 
	"rssi" : -95.0, 
	"snr" : 18.0,
	"snr_max" : 32.0, 
	"snr_min" : 12.0, 
	"macAddr" : "0000000012345611", 
	"data" : "b000168", 
	"frameCnt" : 11, 
	"fport" : 15
}

db = MySQLdb.connect(host="db4free.net", user="nthuee", passwd="nthu1122", db="mqtt_db", charset="utf8")
cursor = db.cursor()
cursor.execute(insert_stmt, data)
db.commit()
db.close()


# db = MySQLdb.connect(host="localhost", user="phpmyadmin", passwd="1122", db="mqtt_db", charset="utf8")
# cursor = db.cursor()

# cursor.execute('INSERT INTO iot_test (channel, sf, time, gwip, gwid, repeater,systype,rssi,snr,snr_max,snr_min,macAddr,data,frameCnt,fport) '
	# 'VALUES (923375000, 10, "2018-06-14T11:35:19", "140.114.71.156", "00001c497b431e9f", "00000000ffffffff", 18, -95.0, 18.0, 32.0, 12.0, 0000000012345611, "b000168",11,15);')
# db.commit()

# db.close()
