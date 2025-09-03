import cv2
import RPi.GPIO as GPIO
import time

# === Servo Setup ===
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz
pwm.start(0)

def set_angle(angle):
    duty = 2 + (angle / 18)
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

# === Camera Setup ===
cap = cv2.VideoCapture(0)  # Pi Camera detected as video0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to HSV for color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Example: Detect "Tin" (let’s say gray/silver range)
    lower_tin = (0, 0, 50)
    upper_tin = (180, 50, 200)
    mask_tin = cv2.inRange(hsv, lower_tin, upper_tin)

    # Example: Detect "Plastic" (bright colors, e.g. red)
    lower_plastic = (0, 100, 100)
    upper_plastic = (10, 255, 255)
    mask_plastic = cv2.inRange(hsv, lower_plastic, upper_plastic)

    # Decision based on detection
    if cv2.countNonZero(mask_tin) > 5000:
        print("Tin detected → Servo Clockwise")
        set_angle(0)   # Clockwise
    elif cv2.countNonZero(mask_plastic) > 5000:
        print("Plastic detected → Servo Anti-Clockwise")
        set_angle(180) # Anti-Clockwise
    
    # Show frame
    cv2.imshow("Frame", frame)

    # Exit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pwm.stop()
GPIO.cleanup()
