# Build Workspace to see changes in Launch Files output

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable
def generate_launch_description():
    package_share_dir = get_package_share_directory("spiral_maze")
    gazebo_ros_package = get_package_share_directory('gazebo_ros')
    gazebo_launch_file = os.path.join(gazebo_ros_package, 'launch', 'gazebo.launch.py')
    world_file = os.path.join(package_share_dir, 'world', 'spiral_maze_course.world')
    return LaunchDescription([
        SetEnvironmentVariable(
            'GAZEBO_MODEL_PATH',
            os.path.join(package_share_dir, 'models') + ':' + os.environ.get('GAZEBO_MODEL_PATH', '')
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_launch_file),
            #launch_arguments={'world': world_file}.items(),
        ),
    ])