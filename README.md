🥤 Tin vs Plastic Detection with Raspberry Pi 5 + Servo Motor
📖 Project Overview

This project uses a Raspberry Pi 5 (8GB) with a Pi Camera and a Servo Motor to detect whether an object is Tin or Plastic.

If Tin is detected → Servo moves clockwise (0°)

If Plastic is detected → Servo moves anti-clockwise (180°)

Detection is done using OpenCV (Python) with simple color filtering.

🛠️ Hardware Components

Raspberry Pi 5 (8GB RAM)

Raspberry Pi Camera (compatible with Pi 5 connector)

180° Servo Motor (SG90 / MG90S)

Jumper wires

(Optional) External 5V Power Supply for servo

🔌 Hardware Connections
Servo Motor Wiring
Servo Pin	Connect to Raspberry Pi
Brown / Black (GND)	Pin 6 (GND)
Red (VCC, 5V)	Pin 2 (5V)
Orange / Yellow (Signal)	Pin 12 (GPIO18, PWM)
Camera Connection

Connect the Pi Camera ribbon cable to the CAM/DISP 0 port.

Ensure the blue side faces the Ethernet port.
