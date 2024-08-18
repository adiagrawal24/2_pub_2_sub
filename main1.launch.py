#!/usr/bin/env python3

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        # Launch the publisher1 node
        launch_ros.actions.Node(
            package='pkg1',  # Replace with your package name
            executable='new_pub.py',  # Name of the executable for the publisher
            name='first_publisher',
            output='screen'),

        # Launch the subscriber1 & publisher2 node
        launch_ros.actions.Node(
            package='pkg1',  # Replace with your package name
            executable='new_sub_pub.py',  # Name of the executable for the subscriber
            name='first_subscriber',
            output='screen'),

        # Launch the subscriber2 node
        launch_ros.actions.Node(
            package='pkg1',  # Replace with your package name
            executable='new_sub.py',  # Name of the executable for the subscriber
            name='second_subscriber',
            output='screen'),
    ])

