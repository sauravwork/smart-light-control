import paho.mqtt.client as mqtt

BROKER = "localhost"
SENSOR_TOPIC = "home/sensor"
LIGHT_TOPIC = "home/light"

# Use new callback API version
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER)

def on_message(client, userdata, msg):
    motion, light = msg.payload.decode().split(",")
    motion = motion == "True"

    if motion and light == "Dark":
        client.publish(LIGHT_TOPIC, "ON")
        print("[Controller] Motion & Dark → Light ON")
    else:
        client.publish(LIGHT_TOPIC, "OFF")
        print("[Controller] No motion/bright → Light OFF")

client.subscribe(SENSOR_TOPIC)
client.on_message = on_message
client.loop_forever()
