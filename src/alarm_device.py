from gpiozero import MotionSensor
from gpiozero import Buzzer
from classes.network import Network
import time

# Network setup
server = Network(12345)

# Buzzer setup
bz = Buzzer(14)

# MotionSensor setup
ms = MotionSensor(17)

while True:
    ms.wait_for_motion()
    print("Motion detected!")
    server.alert("Motion detected!")
    bz.on()
    time.sleep(3)
    bz.off()
