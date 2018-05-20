# Background Keyboard Hook Driver for ROS

## Installation:
   - catkin_make will setup prepare environment 

## Usage: 

`rosrun xlib_keyboard_driver keyboard_driver_node.py`

Press "ESC" at anywhere will automatically shutdown the node.

### Publishing Topics

- "/keyboard/key_up" (std_msgs/String)
    - publishing key which being released

- "/keyboard/key_down" (std_msgs/String)
    - publishing key which being pressed
