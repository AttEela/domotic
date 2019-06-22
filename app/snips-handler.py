import os
import json
import paho.mqtt.client as mqtt

from utils.logger import LogManager
from domotic.domotic_manager import DomoticManager
from domotic.snips.slots_to_actions import snips_slots_to_actions

domotic_manager = DomoticManager()
log_manager = LogManager()
logger = log_manager.logger


def on_connect(client, userdata, flags, rc):
    logger.info("Connected to {0} with result code {1}".format(HOST, rc))
    # Subscribe to the hotword detected topic
    client.subscribe("hermes/hotword/default/detected")
    # Subscribe to any topic starting with 'hermes/intent/'
    client.subscribe('hermes/intent/#')


def on_message(client, userdata, msg):
    if msg.topic == 'hermes/hotword/default/detected':
        logger.info("Hotword detected!")
    elif msg.topic == 'hermes/intent/' + os.environ.get("DOMOTIC_INTENT"):
        payload = json.loads(msg.payload)
        slots = payload["slots"]
        logger.info(snips_slots_to_actions(slots, logger))
        # if slots[0]['rawValue'] == 'eteins':
        #     if slots[1]['rawValue'] == 'télé':
        #         domotic_manager.tv_controller.power_off()


if __name__ == '__main__':

    HOST = 'localhost'
    PORT = 1883  # default port for mqtt on raspberry

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()
