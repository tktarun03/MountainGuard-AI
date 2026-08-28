import json
import os
import paho.mqtt.client as mqtt
from pydantic import ValidationError
from ingestion.schemas import GNSSReading, SeismicReading, WeatherReading, RiverReading

SCHEMAS = {
    "gnss": GNSSReading,
    "seismic": SeismicReading,
    "weather": WeatherReading,
    "river": RiverReading,
}

def parse_message(topic: str, payload: bytes):
    sensor_type = topic.split('/')[1]
    model = SCHEMAS.get(sensor_type)
    if not model:
        raise ValueError(f"Unsupported sensor type: {sensor_type}")
    return model.model_validate(json.loads(payload.decode('utf-8')))

def on_message(client, userdata, msg):
    try:
        reading = parse_message(msg.topic, msg.payload)
        print(f"VALID {msg.topic}: {reading.model_dump_json()}")
    except (ValueError, json.JSONDecodeError, ValidationError) as exc:
        print(f"REJECTED {msg.topic}: {exc}")

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect(os.getenv('MQTT_HOST', 'localhost'), int(os.getenv('MQTT_PORT', '1883')))
    client.subscribe('mountainguard/+/+')
    client.loop_forever()

if __name__ == '__main__':
    main()
