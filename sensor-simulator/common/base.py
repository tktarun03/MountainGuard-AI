import json
import os
import time
from datetime import datetime, timezone
import paho.mqtt.client as mqtt

class SensorPublisher:
    def __init__(self):
        self.host = os.getenv('MQTT_HOST', 'localhost')
        self.port = int(os.getenv('MQTT_PORT', '1883'))
        self.interval = float(os.getenv('SIMULATION_INTERVAL_SECONDS', '2'))
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    def connect(self):
        self.client.connect(self.host, self.port)
        self.client.loop_start()

    def publish(self, topic: str, payload: dict):
        payload = {**payload, 'timestamp': datetime.now(timezone.utc).isoformat()}
        self.client.publish(topic, json.dumps(payload))

    def close(self):
        self.client.loop_stop()
        self.client.disconnect()
