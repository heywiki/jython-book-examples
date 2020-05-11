import time
import json

#pip install paho-mqtt
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with result code" + str(rc))

client = mqtt.Client()
client.on_connect = on_connect

#You could use:
#tcp://test.mosquitto.org:1883
client.connect("localhost", 1883, 60)

client.loop_start()

json = """
{
   "source_ts": "2019-10-23T07:07:32.939Z",
   "value": "$val"
}
"""


#json = json.replace("$val", "25");

#temperature = random.randrange(20, 25)
#data = json.loads(json_string)


while True:
    time.sleep(2)
    client.publish("msr145/545016/get/measurement/T1", json)
