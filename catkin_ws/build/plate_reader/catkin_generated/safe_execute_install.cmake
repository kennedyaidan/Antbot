execute_process(COMMAND "/home/smerc/AntBot/catkin_ws/build/plate_reader/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/smerc/AntBot/catkin_ws/build/plate_reader/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
