# 指定CMake最低版本要求
cmake_minimum_required(VERSION 3.0.2)
# 定义功能包名称
project(pcd_convert_pkg)

# 查找ROS catkin相关依赖包，COMPONENTS后面填写需要用到的ROS组件
find_package(catkin REQUIRED COMPONENTS
  pcl_ros        # ROS封装的PCL点云库
  roscpp         # ROS C++客户端接口
  rospy          # ROS Python客户端接口
  rviz           # RViz可视化
  sensor_msgs    # 传感器消息，点云等消息类型
  tf2_ros        # TF坐标变换
)


# 启用Python脚本支持
# catkin_python_setup()



# catkin对外导出配置，供其他功能包调用本包
# INCLUDE_DIRS：导出头文件目录，本包暂无头文件，暂时注释
# LIBRARIES：导出编译生成的库，本包暂无自建库，暂时注释
# CATKIN_DEPENDS：声明本包依赖的ROS功能包列表
# DEPENDS：系统底层依赖
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES pcd_convert_pkg
 CATKIN_DEPENDS pcl_ros roscpp rospy rviz sensor_msgs tf2_ros
#  DEPENDS system_lib
)

# 设置头文件搜索路径
# include：本地include头文件目录，本包暂时没有头文件，注释
# ${catkin_INCLUDE_DIRS}：ROS各个依赖包的头文件路径
include_directories(
# include
${catkin_INCLUDE_DIRS}
)


add_executable(pcd2pgm src/pcd2pgm.cpp)
target_link_libraries(pcd2pgm ${catkin_LIBRARIES} ${PCL_LIBRARIES})
# 安装配置文件、launch文件、地图、RViz配置
install(DIRECTORY config launch maps rviz
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
