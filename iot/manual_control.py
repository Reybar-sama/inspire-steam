from pysimverse import Drone
import time
import cv2
import keyboard

drone = Drone()
drone.connect()
time.sleep(1)

drone.take_off(5)
remctrl_speed = 250

while True:
    key = keyboard.read_key() 

    # get your values to zero
    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0

    if keyboard.is_pressed("w"):
        forward_backward = remctrl_speed
    elif keyboard.is_pressed("s"):
        forward_backward = -remctrl_speed 
    elif keyboard.is_pressed("a"):
        left_right = -remctrl_speed
    elif keyboard.is_pressed("d"):
        left_right = remctrl_speed
    elif keyboard.is_pressed("f"):
        up_down = remctrl_speed
    elif keyboard.is_pressed("c"):
        up_down = -remctrl_speed
    elif keyboard.is_pressed("q"):
        yaw = -1
    elif keyboard.is_pressed("e"):
        yaw = 1
    elif keyboard.is_pressed("1") or key == 27:
        drone.land()
        time.sleep(2)
        break


    drone.send_rc_control(
        left_right,
        forward_backward,
        up_down,
        yaw
    )


