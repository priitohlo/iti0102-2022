import time

from FollowerBot import FollowerBot

robot = FollowerBot()


def test_run(robot: FollowerBot):
    robot.set_wheels_speed(100)
    time.sleep(9)
    robot.set_wheels_speed(0)
    robot.done()
