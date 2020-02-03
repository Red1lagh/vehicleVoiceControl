import RPi.GPIO as GPIO
import time

print("c est bon servo")

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5

pwm=GPIO.PWM(18,100)
pwm.start(5)

angle1 = 0
duty1 = float(angle1)/10 + ajoutAngle
angle2=180
duty2= float(angle2)/10 + ajoutAngle
pwm.ChangeDutyCycle(duty1)
time.sleep(0.8)
pwm.ChangeDutyCycle(duty2)
time.sleep(0.8)
GPIO.cleanup()
