from gpiozero import MotionSensor
from gpiozero import Buzzer

pir = MotionSensor(17)
bz = Buzzer(23)
while True: 
    if pir.motion_detected:
        print("TEST")
        bz.on()
