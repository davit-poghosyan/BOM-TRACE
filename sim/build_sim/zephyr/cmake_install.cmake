# Install script for directory: /home/davit/Desktop/sim/zephyr

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
  include("/home/davit/Desktop/sim/build_sim/zephyr/arch/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/lib/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/soc/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/boards/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/subsys/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/drivers/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/modules/vcp/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/modules/queue-chan/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/modules/scope/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/modules/cmsis/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/modules/hal_wch/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/modules/littlefs/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/modules/mbedtls/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/modules/mcuboot/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/kernel/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/cmake/flash/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/cmake/usage/cmake_install.cmake")
  include("/home/davit/Desktop/sim/build_sim/zephyr/cmake/reports/cmake_install.cmake")

endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/home/davit/Desktop/sim/build_sim/zephyr/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
