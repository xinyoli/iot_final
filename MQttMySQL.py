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
		json_data = json.loads(message_)[0]
		print(type(json_data))
		print(json_data)
		
		insert_stmt = (
			"INSERT INTO iot_test (channel, sf, time, gwip, gwid, repeater,systype,rssi,snr,snr_max,snr_min,macAddr,data,frameCnt,fport)"
			"VALUES (%d, %d, %s, %s, %s, %s, %d, %f, %f, %f, %f, %d, %s, %d, %d)"
		)
		data = (\
			json_data['channel'], \
			json_data['sf'], \
			json_data['time'], \
			json_data['gwip'], \
			json_data['gwid'], \
			json_data['repeater'], \
			json_data['systype'], \
			json_data['rssi'], \
			json_data['snr'], \
			json_data['snr_max'], \
			json_data['snr_min'], \
			json_data['macAddr'], \
			json_data['data'], \
			json_data['frameCnt'], \
			json_data['fport'] \
		)
		db = MySQLdb.connect(host="localhost", user="phpmyadmin", passwd="1122", db="mqtt_db", charset="utf8")
		cursor = db.cursor()
		cursor.execute(insert_stmt, data)
		db.commit()
		db.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("167.99.224.125", 1883, 60)
client.loop_forever()

