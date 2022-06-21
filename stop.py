import RPi.GPIO as GPIO
import time
import ultrasonic

from TCPClient import TCPClient
from Command import COMMAND as cmd
from gpiozero import LED, Button
from time import sleep

print("Test1 demo pgrogram")
print("-------------------")

followerL = 25
GPIO.setup(followerL, GPIO.IN)

followerR = 17
GPIO.setup(followerR, GPIO.IN)

SERVER_IP="localhost"

SERVO_MIN_ANGLE = 0
SERVO_MAX_ANGLE = 180

tcp = TCPClient()

print("Connecting ...", SERVER_IP)

try:
    tcp.connectToServer(address = (SERVER_IP, 12345))
except Exception as e:
    print("Connection to server", SERVER_IP, "failed!")
    exit(1)

print("Connection Successful !")

tcp.sendData(cmd.CMD_STOP)

tcp.disConnect()
GPIO.cleanup()
