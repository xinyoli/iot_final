# SubscriberTest.py
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("GIOT-GW/UL/1C497B43217A")
    # client.subscribe("MYTOPIC")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload), "\n")
	message_ = msg.payload.decode("utf-8")
	print(type(message_))
	print(message_, "\n")
	# msg_json = json.loads(message_)
	# print(type(msg_json))
	# print(msg_json)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("167.99.224.125", 1883, 60)
client.loop_forever()

