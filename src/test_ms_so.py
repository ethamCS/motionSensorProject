import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7

GPIO.setup(PIR_PIN, GPIO.IN)

print("Setup complete...")
print("Starting script")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("MOTION DETECTED")
		else:
            print("NO MOTION")
        time.sleep(1)
except KeyboardInterrupt:
    print("Quitting")
    GPIO.cleanup()
