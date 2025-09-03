# Raspberry Pi 5 – Tin vs Plastic Detection with Servo Control

This project uses a **Raspberry Pi 5 (8GB RAM)**, **Pi Camera**, and a **servo motor** to detect whether an object is **Tin** or **Plastic** using **OpenCV**.  
If Tin is detected → the servo rotates **clockwise**.  
If Plastic is detected → the servo rotates **anti-clockwise**.  

---

## 🛠️ Hardware Requirements
- Raspberry Pi 5 (8GB model recommended)
- Raspberry Pi Camera Module (compatible with Pi 5 ribbon connector)
- Servo Motor (SG90, MG90S, or similar 180° servo)
- Jumper wires
- Optional: External 5V power supply for servo (recommended if using high torque servo)

---

## 🔌 Hardware Connections

### Camera
- Connect the Pi Camera to **CAM/DISP 0** (near USB ports).  
- Ensure the ribbon cable is inserted with the **blue side facing the Ethernet port**.

### Servo Motor Wiring
| Servo Wire  | Raspberry Pi Pin |
|-------------|------------------|
| Brown/Black (GND) | Pin **6** (GND) |
| Red (VCC 5V)      | Pin **2** (5V) |
| Orange/Yellow (Signal) | Pin **12** (GPIO18, PWM) |

⚠️ If using an external 5V power supply for the servo, connect the grounds together.

---

## 📦 Software Installation

Update system first:
```bash
sudo apt update && sudo apt upgrade -y
