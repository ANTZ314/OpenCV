
cmake_minimum_required(VERSION 2.8)
project( ObjDet )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( ObjDet ObjDet.cpp )
target_link_libraries( ObjDet ${OpenCV_LIBS} )
