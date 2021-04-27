from RPi.GPIO as GPIO
from gpiozero import Buzzer
from classes.network import Network
import time

# Network setup
server = Network(12345)

# Buzzer setup
bz = Buzzer(17)

# MotionSensor setup
GPIO.setmode(GPIO.BCM)
MS_PIN = 7

GPIO.setup(MS_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(MS_PIN):
            print("Motion detected!")
            server.alert_server("Motion detected!")
            bz.on()
            time.sleep(3)
            bz.off()
except KeyboardInterrupt:
    print("Quitting")
    server.close_connection()
