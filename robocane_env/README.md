# Launch robocane_env (raw)

In order to launch the enviroment it is required to:

- inside a workspace create catkin package called "robocane_manual"
- build + source it
- in sourced terminal start the launch file of robocane_manual called "robocane.launch"

Step by step:
- go into an existing workspace (or create new one if wanted)
- `catkin create pkg robocane_manual && cd robocane_manual`
- `git clone git@github.com:pkehr/robocane_env.git`
- build workspace and source it
- `roslaunch robocane_manual robocane.launch`
