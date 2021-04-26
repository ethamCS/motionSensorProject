from gpiozero import MotionSensor

pir = MotionSensor(17,threshold=.99)
pir.wait_for_motion()
print("Motion detected!")
