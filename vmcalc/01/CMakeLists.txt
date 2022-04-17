cmake_minimum_required(VERSION 3.0)
project(vmcalc C)

set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DDEBUG_TRACE_EXECUTION")
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DDEBUG_PRINT_CODE")

include_directories(include)

add_executable(vmcalc
  src/main.c
  src/io.c
)
