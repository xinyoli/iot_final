import paho.mqtt.client as mqtt
import json
import MySQLdb

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("GIOT-GW/UL/1C497B43217A")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload), "\n")
	message_ = msg.payload.decode("utf-8")
	print(type(message_))
	print(message_, "\n")
	
	if message_ != "hello" : 
	
		try:
		
			json_data = json.loads(message_)[0]
			print(type(json_data))
			print(json_data)
			
			# print(type(json_data['channel']))
			# print(json_data['channel'])
			# print(type(json_data['sf']))
			# print(json_data['sf'])
			# print(type(json_data['time']))
			# print(json_data['time'])
			# print(type(json_data['gwip']))
			# print(json_data['gwip'])
			# print(type(json_data['gwid']))
			# print(json_data['gwid'])
			# print(type(json_data['repeater']))
			# print(json_data['repeater'])
			# print(type(json_data['systype']))
			# print(json_data['systype'])
			# print(type(json_data['rssi']))
			# print(json_data['rssi'])
			# print(type(json_data['snr']))
			# print(json_data['snr'])
			# print(type(json_data['snr_max']))
			# print(json_data['snr_max'])
			# print(type(json_data['snr_min']))
			# print(json_data['snr_min'])
			# print(type(json_data['macAddr']))
			# print(json_data['macAddr'])
			# print(type(json_data['data']))
			# print(json_data['data'])
			# print(type(json_data['frameCnt']))
			# print(json_data['frameCnt'])
			# print(type(json_data['fport']))
			# print(json_data['fport'])
			
			insert_stmt = (
				"INSERT INTO iot_test (channel, sf, time, gwip, gwid, repeater,systype,rssi,snr,snr_max,snr_min,macAddr,data,frameCnt,fport)"
				"VALUES (%d, %d, %s, %s, %s, %s, %d, %f, %f, %f, %f, %s, %s, %d, %d)"
			)
			data = (\
				int(json_data['channel']), \
				int(json_data['sf']), \
				str(json_data['time']), \
				str(json_data['gwip']), \
				str(json_data['gwid']), \
				str(json_data['repeater']), \
				int(json_data['systype']), \
				float(json_data['rssi']), \
				float(json_data['snr']), \
				float(json_data['snr_max']), \
				float(json_data['snr_min']), \
				str(json_data['macAddr']), \
				str(json_data['data']), \
				int(json_data['frameCnt']), \
				int(json_data['fport']) \
			)
			db = MySQLdb.connect(host="localhost", user="phpmyadmin", passwd="1122", db="mqtt_db", charset="utf8")
			cursor = db.cursor()
			cursor.execute(insert_stmt, data)
			db.commit()
			db.close()
		except BaseException :
			print("json decoding error!!!")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("167.99.224.125", 1883, 60)
client.loop_forever()

