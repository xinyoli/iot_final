import json
import MySQLdb

string_ = "[	\
{\"channel\":923375000, \
\"sf\":10, \
\"time\":\"2018-06-12T11:35:19\" , \
\"gwip\":\"140.114.71.156\", \
\"gwid\":\"00001c497b431e9f\", \
\"repeater\":\"00000000ffffffff\", \
\"systype\":18, \
\"rssi\":-95.0, \
\"snr\":18.0, \
\"snr_max\":32.0, \
\"snr_min\":12.0, \
\"macAddr\":\"0000000012345611\", \
\"data\":\"b000\", \
\"frameCnt\":11, \
\"fport\":15}	\
]"
print(type(string_))
print(string_)
json_data = json.loads(string_)[0]
print(type(json_data))
print(json_data)


print(type(json_data['channel']))
print(json_data['channel'])
print(type(json_data['sf']))
print(json_data['sf'])
print(type(json_data['time']))
print(json_data['time'])
print(type(json_data['gwip']))
print(json_data['gwip'])
print(type(json_data['gwid']))
print(json_data['gwid'])
print(type(json_data['repeater']))
print(json_data['repeater'])
print(type(json_data['systype']))
print(json_data['systype'])
print(type(json_data['rssi']))
print(json_data['rssi'])
print(type(json_data['snr']))
print(json_data['snr'])
print(type(json_data['snr_max']))
print(json_data['snr_max'])
print(type(json_data['snr_min']))
print(json_data['snr_min'])
print(type(json_data['macAddr']))
print(json_data['macAddr'])
print(type(json_data['data']))
print(json_data['data'])
print(type(json_data['frameCnt']))
print(json_data['frameCnt'])
print(type(json_data['fport']))
print(json_data['fport'])

