import time

from FollowerBot import FollowerBot

robot = FollowerBot()


def test_run(robot: FollowerBot):
    robot.set_wheels_speed(20)
    time.sleep(1)
    robot.done()
