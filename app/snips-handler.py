import os
import json
import paho.mqtt.client as mqtt

from domotic.domotic_manager import DomoticManager

HOST = 'localhost'
PORT = 1883  # default port for mqtt on raspberry

domotic_manager = DomoticManager()


def on_connect(client, userdata, flags, rc):
    print("Connected to {0} with result code {1}".format(HOST, rc))
    # Subscribe to the hotword detected topic
    client.subscribe("hermes/hotword/default/detected")
    # Subscribe to any topic starting with 'hermes/intent/'
    client.subscribe('hermes/intent/#')


def on_message(client, userdata, msg):
    if msg.topic == 'hermes/hotword/default/detected':
        print("Hotword detected!")
    elif msg.topic == 'hermes/intent/' + os.environ.get("DOMOTIC_INTENT"):
        payload = json.loads(msg.payload)
        name = payload["intent"]["intentName"]
        slots = payload["slots"]
        print("Intent {0} detected with slots {1}".format(name, slots))
        if slots[0]['rawValue'] == 'eteins':
            if slots[0]['rawValue'] == 'télé':
                domotic_manager.tv_controller.power_off()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(HOST, PORT, 60)
client.loop_forever()
