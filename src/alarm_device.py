from gpiozero import MotionSensor
from gpiozero import Buzzer
from classes.network import Network
import time

# Network setup
server = Network(12345)

# Buzzer setup
bz = Buzzer(17)

# MotionSensor setup
ms = MotionSensor(7)

try:
while True:
    if ms.motion_detected:
        print("Motion detected!")
        server.alert_server("Motion detected!")
        bz.on()
        time.sleep(3)
        bz.off()
except KeyboardInterrupt:
    print("Quitting")
    server.close_connection()
