from gpiozero import MotionSensor

pir = MotionSensor(17,threshold=.9)
pir.wait_for_motion()
print("Motion detected!")
