import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC = "home/light"

def on_message(client, userdata, msg):
    status = msg.payload.decode()
    if status == "ON":
        print("[Light Bulb] 💡 Light is ON")
    else:
        print("[Light Bulb] ❌ Light is OFF")

client = mqtt.Client()
client.connect(BROKER)
client.subscribe(TOPIC)
client.on_message = on_message
client.loop_forever()
