from gpiozero import MotionSensor

pir = MotionSensor(17,threshold=1)
pir.wait_for_motion()
print("Motion detected!")
