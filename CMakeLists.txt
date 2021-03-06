cmake_minimum_required(VERSION 2.8)

set(CMAKE_C_COMPILER "clang2")
set(CMAKE_CXX_COMPILER "${CMAKE_C_COMPILER}")

project(lempitsky)
set(CMAKE_BUILD_TYPE "Release")

# MacPorts
include_directories(/opt/local/include)
link_directories(/opt/local/lib)

message(STATUS "Checking OpenCV")
find_package( OpenCV REQUIRED )
include_directories(${OpenCV_INCLUDE_DIRS})
set(OpenCV_LIBS opencv_core opencv_highgui opencv_imgproc)

message(STATUS "Checking OpenMP")
find_package(OpenMP REQUIRED)
IF(OPENMP_FOUND)
	# add flags for OpenMP
	set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
	set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS}	OpenMP_SHARED_LINKER_FLAGS}")
	set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
ENDIF()

# Add flags to support clang2
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -stdlib=libstdc++")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libstdc++")
set(CMAKE_SHARED_LINKER_FLAGS "-lstdc++ -stdlib=libstdc++")
set(CMAKE_EXE_LINKER_FLAGS "-lstdc++ -stdlib=libstdc++")

set(SOURCE_FILES 
	__SOURCE_FILES__)

add_executable(py__SHORT__exe ${SOURCE_FILES})

add_library(py__SHORT__ SHARED 
	src/py__SHORT__.cpp
	${SOURCE_FILES})

target_link_libraries(py__SHORT__ "${OpenCV_LIBS} -lstdc++ -stdlib=libstdc++")
target_link_libraries(py__SHORT__exe "${OpenCV_LIBS}")



