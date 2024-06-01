from launch import LaunchDescription
from launch_ros.actions import Node 
import os
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():


    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager"
        ]
    )

    gg_hexleg_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "gg_hexleg_controller",
            "--controller-manager",
            "/controller_manager"
        ]
    )


    return LaunchDescription(
        [
            joint_state_broadcaster_spawner,
            gg_hexleg_controller_spawner
        ]
    )
