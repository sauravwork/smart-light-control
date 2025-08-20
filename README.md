# 💡 Smart Light Control (IoT Simulation Project)

This project simulates an **IoT-based Smart Light Control System** without using real hardware.  
It demonstrates how IoT devices (sensors & actuators) communicate via **MQTT protocol**,  
and how a central controller automates the process of turning lights ON/OFF.

---

## 🔹 Features
- Simulated **motion/ambient light sensor**
- Simulated **smart light bulb**
- **MQTT communication** between devices
- **Automatic control** based on conditions:
  - If motion detected **and** ambient light is dark → Light ON
  - Otherwise → Light OFF
- **Dashboard (Flask)** for manual ON/OFF control and monitoring

---

## 🔹 Folder Structure
smart-light-control/
│── README.md # Documentation
│── requirements.txt # Python dependencies
│── sensor_simulator.py # Virtual motion/ambient light sensor
│── light_bulb_simulator.py # Virtual smart light bulb
│── controller.py # IoT logic (automation rules)
│── dashboard.py # Web dashboard for control