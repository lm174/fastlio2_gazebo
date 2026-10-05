#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""键盘控制节点: WASD控制小车缓慢移动"""

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

# 慢速参数
LINEAR_SPEED = 0.1   # 线速度 m/s
ANGULAR_SPEED = 0.2  # 角速度 rad/s

def get_key():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, settings)
    return key

if __name__ == '__main__':
    rospy.init_node('keyboard_control')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    settings = termios.tcgetattr(sys.stdin)

    print("===== 键盘控制 =====")
    print("W: 前进    S: 后退")
    print("A: 左转    D: 右转")
    print("空格: 停止  Q: 退出")
    print("===================")

    twist = Twist()
    while not rospy.is_shutdown():
        key = get_key()
        if key == 'w':
            twist.linear.x = LINEAR_SPEED
            twist.angular.z = 0.0
        elif key == 's':
            twist.linear.x = -LINEAR_SPEED
            twist.angular.z = 0.0
        elif key == 'a':
            twist.linear.x = 0.0
            twist.angular.z = ANGULAR_SPEED
        elif key == 'd':
            twist.linear.x = 0.0
            twist.angular.z = -ANGULAR_SPEED
        elif key == ' ':
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        elif key == 'q':
            break

        pub.publish(twist)

    # 退出时发布零速度
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, settings)
