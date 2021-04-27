from gpiozero import MotionSensor
import time

ms = MotionSensor(7, threshold=.99)

print("Setup complete...")
print("Starting script")

while True:
    if ms.motion_detected:
        print("MOTION DETECTED")
    else:
        print("NO MOTION")
    time.sleep(1)
