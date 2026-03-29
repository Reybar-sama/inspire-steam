from pysimverse import Drone
import time

drone = Drone()
drone.connect()
time.sleep(1)


drone.take_off(50)
drone.move_forward(250)
drone.move_right(250)
drone.land(50)
