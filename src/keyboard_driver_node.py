#!/usr/bin/env python

from hook_manager import HookManager
import rospy
from std_srvs.srv import Empty
from std_msgs.msg import String

# A ROS Node to hook keyboard input from xserver using python-xlib


class KeyboardDriverNode:
    def __init__(self):
        rospy.init_node('xlib_keyboard_driver', anonymous=False)
        rospy.loginfo("---Start Hooking Keyboard from Xserver----")
        self.shutdown_service = rospy.Service('shutdown_keyboard_driver', Empty, self.shutdown_srv_callback)
        self.hm = HookManager()
        self.hm.HookKeyboard()
        self.key_up_pub = rospy.Publisher('/keyboard/key_up', String, queue_size=1)
        self.key_down_pub = rospy.Publisher('/keyboard/key_down', String, queue_size=1)
        # Register Keyboard Hook Callback
        self.hm.KeyUp = self.key_up_callback
        self.hm.KeyDown = self.key_down_callback
        self.hm.start()
        rospy.on_shutdown(self.shutdown_node)
        rospy.spin()

    def key_up_callback(self, data):
        # when release
        self.key_up_pub.publish(String(data.Key))

    def key_down_callback(self, data):
        # when push
        if data.Key == 'Escape':
            print("---Exiting Keyboard Hook Node---")
            self.shutdown_node()

        self.key_down_pub.publish(String(data.Key))

    def shutdown_srv_callback(self, req):
        self.shutdown_node()

    def shutdown_node(self):
        self.hm.cancel()
        rospy.signal_shutdown("Shutting down xlib Keyboard Driver")


if __name__ == '__main__':
    KeyboardDriverNode()


