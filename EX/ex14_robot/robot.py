import time

from FollowerBot import FollowerBot

robot = FollowerBot()


def test_run(robot: FollowerBot):
    robot.set_wheels_speed(20)
    time.sleep(100)
    robot.set_wheels_speed(0)
    robot.done()
