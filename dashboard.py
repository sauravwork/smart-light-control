from flask import Flask, render_template_string, request
import paho.mqtt.publish as publish

BROKER = "localhost"
LIGHT_TOPIC = "home/light"

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
  <title>Smart Light Dashboard</title>
</head>
<body style="font-family:Arial;text-align:center;margin-top:50px;">
  <h1>💡 Smart Light Control</h1>
  <form method="post">
    <button name="action" value="ON">Turn ON</button>
    <button name="action" value="OFF">Turn OFF</button>
  </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        action = request.form["action"]
        publish.single(LIGHT_TOPIC, action, hostname=BROKER)
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
