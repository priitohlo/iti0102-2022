"""docstring."""
from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(1)
    robot.sleep(9)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(17)
    while robot.get_left_line_sensor() != 0 and robot.get_right_line_sensor() != 0:
        robot.sleep(1)
    robot.sleep(1)
    robot.done()


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(6)

    while robot.get_left_line_sensor() != 0 and robot.get_right_line_sensor() != 0:
        robot.sleep(1)
        print(robot.get_line_sensors())

    while robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() == 0:
        if all(v == 0 for v in robot.get_right_line_sensors()):
            robot.set_wheels_speed(0)
            robot.set_left_wheel_speed(1)
            robot.sleep(1)
            robot.set_left_wheel_speed(0)
            robot.set_wheels_speed(6)
        robot.sleep(1)
        print(robot.get_line_sensors())

    print(robot.get_line_sensors())

    # while 0 in robot.get_line_sensors():
    #     if all(v == 0 for v in robot.get_left_line_sensors()) and \
    #             all(v == 0 for v in robot.get_right_line_sensors()):
    #         robot.sleep(1)

    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """


if __name__ == '__main__':
    follow_the_line(FollowerBot(track_image='uturn.png', starting_orientation=90, start_x=122, start_y=270))
