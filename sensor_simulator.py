import paho.mqtt.client as mqtt
import time
import random

# MQTT Broker details
BROKER = "localhost"   # Change if using a remote broker
TOPIC = "home/sensor"

# Connect with new callback API version
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER)

print("[Sensor] Simulator started...")

while True:
    # Simulate motion detected or not
    motion = random.choice([True, False])
    # Simulate ambient light condition
    light = random.choice(["Dark", "Bright"])

    # Create message as "True,Dark" or "False,Bright"
    payload = f"{motion},{light}"
    
    # Publish to broker
    client.publish(TOPIC, payload)
    print(f"[Sensor] Motion: {motion}, Light: {light}")

    # Wait for 3 seconds before sending next reading
    time.sleep(3)
