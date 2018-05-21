#!/usr/bin/env python
import rospy

import tf
# import turtlesim.msg
from std_msgs.msg import String

def callback(msg):
    pass
  

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    rospy.Subscriber('/keyboard/key_down', String, callback,
     queue_size=10)
    rate = rospy.Rate(20)
    br = tf.TransformBroadcaster()
    while not rospy.is_shutdown():
        br.sendTransform((0.5, 0.5, 0),
                     tf.transformations.quaternion_from_euler(0, 0, 0),
                     rospy.Time.now(),
                     "/base_link",
                     "/world")
        rate.sleep()
