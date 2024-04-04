#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int8

def control_motor():
    rospy.init_node('motor_controller', anonymous=True)
    motor_pub = rospy.Publisher('motor_cmd', Int8, queue_size=10)

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        command = input("Enter command: '5' for forward, '2' for backward, '1' for left, '3' for right, '0' to stop: ")
        try:
            command = int(command)
            if command in [5, 3, 0, 1, 2]:
                motor_pub.publish(command)
            else:
                rospy.logwarn("Invalid command. Enter '1' for left, '2' for backward, '0' to stop, '5' for forward, '3' for right.")
        except ValueError:
            rospy.logwarn("Invalid command. Enter '1' for left, '2' for backward, '0' to stop, '5' for forward, '3' for right.")

        rate.sleep()

if __name__ == '__main__':
    try:
        control_motor()
    except rospy.ROSInterruptException:
        pass

