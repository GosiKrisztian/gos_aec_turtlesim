from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package='gos_aec_turtlesim',
                executable='rajz',
                output='screen'
            ),
            Node(
                package='turtlesim',
                executable='turtlesim_node',
            ),
        ]
    )