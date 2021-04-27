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

print("Warming up")
i = 100000000
while i > 0:
    i = i - 1
print("Done warming up")

try:
    while True:
        if ms.motion_detected:
            print("Motion detected!")
            server.alert_server("Motion detected!")
            bz.on()
            time.sleep(5)
            bz.off()
except KeyboardInterrupt:
    print("Quitting")
    server.close_connection()
