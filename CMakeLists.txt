cmake_minimum_required(VERSION 3.8)
project(robocane_manual)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
  PATTERN "__pycache__" EXCLUDE
  PATTERN "*.pyc" EXCLUDE
)

install(
  DIRECTORY robocane_env
  DESTINATION share/${PROJECT_NAME}
)

install(
  FILES resource/${PROJECT_NAME}
  DESTINATION share/ament_index/resource_index/packages
)

ament_package()
