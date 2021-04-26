from gpiozero import MotionSensor
from gpiozero import Buzzer
from classes.network import Network
import time

# Network setup
server = Network(12345)

# Buzzer setup
bz = Buzzer(23)

# MotionSensor setup
ms = MotionSensor(17)
i = 0
while i < 1000000:
    i = i + 1
print("Done warming up")

while True:
    ms.wait_for_motion()
    print("Motion detected!")
    server.alert_server("Motion detected!")
    bz.on()
    time.sleep(3)
    bz.off()
