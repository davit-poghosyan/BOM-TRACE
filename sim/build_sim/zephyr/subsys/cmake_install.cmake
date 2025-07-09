# Install script for directory: /home/davit/Desktop/sim/zephyr/subsys

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "TRUE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/home/davit/zephyr-sdk-0.16.8/riscv64-zephyr-elf/bin/riscv64-zephyr-elf-objdump")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/canbus/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/debug/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/fb/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/fs/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/ipc/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/logging/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/mem_mgmt/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/mgmt/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/modbus/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/pm/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/portability/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/random/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/rtio/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/sd/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/stats/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/storage/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/task_wdt/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/testsuite/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/tracing/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/usb/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/dfu/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/net/cmake_install.cmake")

endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/home/davit/Desktop/sim/build_sim/zephyr/subsys/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
