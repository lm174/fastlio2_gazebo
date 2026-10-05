cmake_minimum_required(VERSION 3.0.2)
# 包名，和package.xml的name保持一致
project(fastlio_sim)

# 指定C++标准，适配FAST‑LIO相关代码
add_compile_options(-std=c++17)

# 查找catkin依赖包，用到的ROS组件写在COMPONENTS内
find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  roscpp
  std_msgs
  urdf
  xacro
)

# catkin导出配置，供其他包依赖本包使用
# CATKIN_DEPENDS：填写本包依赖的ROS包列表
catkin_package(
  CATKIN_DEPENDS gazebo_ros roscpp std_msgs urdf xacro
)

# 设置头文件查找路径
include_directories(
  ${catkin_INCLUDE_DIRS}
)

# ============ 添加C++节点示例 ============
# 当src目录下新增cpp源码时，取消下面注释，修改节点名与cpp文件名
# add_executable(sim_node src/sim_node.cpp)        # 根据cpp生成可执行节点
# target_link_libraries(sim_node ${catkin_LIBRARIES}) # 链接catkin库
# add_dependencies(sim_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS}) # 消息生成依赖
