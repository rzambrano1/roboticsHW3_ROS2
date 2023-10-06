==============
ROS2 Version
============

Humble Hawksbill

Installation Guide:
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

==============
Gazebo Version
==============

Gazebo multi-robot simulator, version 11.10.2

Installation Guide:
https://classic.gazebosim.org/tutorials?tut=install_ubuntu

==================================
Installing gazebo_ros_pkgs (ROS 2)
==================================

http://classic.gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros

=================
SDF Format Guides
=================

http://sdformat.org/

========================
Reproducing the Scenario
========================

(1) Open the .world file

$gazebo dogJr_v2.world

(2) Save the model files in the /.gazebo/models/dogJr/

The model files are:

model.config
model.sdf

The sdf code is based on a demo car. I extended this file with the laser scan device and the corresponding joint.

(3) Insert the dogJr model in the scene

Go to the inter tab and click on dogJr, then insert the model directly into the scene

(4) Once the ROS2 workspace is setup and the dogJr controller is installed in the scr folder run the package with the following command:

$ ros2 run dogJr_controller car_controller

NOTE1: To stop the car on might need to have the keyboard operation in place. To get the keyboard operation run :

$ ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/demo/cmd_demo

This command remaps the output messages of the /teleop_twist_keyboard node to the /demo/cmd/_demo topic (the topic to which the /demo/diff_drive node is subscribed

NOTE2: To see the messages published by  the /teleop_twist_keyboard node run:

$ ros2 topic echo /demo/cmd_demo

NOTE3: To verify the nodes and the topics run:

$ rqt_graph



