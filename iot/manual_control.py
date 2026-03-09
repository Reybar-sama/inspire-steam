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
    key = keyboard.read_key() & 0xff

    # get your values to zero
    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0

    if key == ord("w"):
        forward_backward = remctrl_speed
    elif key == ord("s"):
        forward_backward = -remctrl_speed 
    elif key == ord("a"):
        left_right = -remctrl_speed
    elif key == ord("d"):
        left_right = remctrl_speed
    elif key == ord("f"):
        up_down = remctrl_speed
    elif key == ord("c"):
        up_down = -remctrl_speed
    elif key == ord("q"):
        yaw = -1
    elif key == ord("e"):
        yaw = 1
    elif key == ord("1") or key == 27:
        drone.land()
        time.sleep(2)
        break


    drone.send_rc_control(
        left_right,
        forward_backward,
        up_down,
        yaw
    )


