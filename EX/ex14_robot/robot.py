from FollowerBot import FollowerBot

robot = FollowerBot()


def test_run(robot: FollowerBot):
    robot.set_wheels_speed(20)
    sleep(1)
    robot.done()
