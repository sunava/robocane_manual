from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node


def generate_launch_description():
    package_share = get_package_share_directory("robocane_manual")
    default_urdf = f"{package_share}/robocane_env/robocane.urdf"
    default_rviz = f"{package_share}/robocane_env/rviz_config/config.rviz"

    urdf_file = LaunchConfiguration("urdf_file")
    gui = LaunchConfiguration("gui")
    rviz_config = LaunchConfiguration("rviz_config")

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "urdf_file",
                default_value=str(default_urdf),
                description="Absolute path to the URDF file.",
            ),
            DeclareLaunchArgument(
                "rviz_config",
                default_value=str(default_rviz),
                description="Absolute path to the RViz config file.",
            ),
            DeclareLaunchArgument(
                "gui",
                default_value="true",
                description="Start joint_state_publisher_gui.",
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[
                    {
                        "robot_description": ParameterValue(
                            Command(["cat ", urdf_file]),
                            value_type=str,
                        ),
                    }
                ],
            ),
            Node(
                package="joint_state_publisher_gui",
                executable="joint_state_publisher_gui",
                name="joint_state_publisher_gui",
                condition=IfCondition(gui),
                output="screen",
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                arguments=["-d", rviz_config],
                output="screen",
            ),
        ]
    )
