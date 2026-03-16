# robocane_manual

ROS 2 package for loading the RoboCane environment URDF and visualizing it in RViz 2.

## Build

From your ROS 2 workspace root:

```bash
colcon build --packages-select robocane_manual
source install/setup.bash
```

## Run

```bash
ros2 launch robocane_manual robocane.launch.py
```

To disable the joint state publisher GUI:

```bash
ros2 launch robocane_manual robocane.launch.py gui:=false
```
