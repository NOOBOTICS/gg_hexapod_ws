// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from arm_interface_pkg:srv/QuaternionToEuler.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACE_PKG__SRV__DETAIL__QUATERNION_TO_EULER__STRUCT_H_
#define ARM_INTERFACE_PKG__SRV__DETAIL__QUATERNION_TO_EULER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/QuaternionToEuler in the package arm_interface_pkg.
typedef struct arm_interface_pkg__srv__QuaternionToEuler_Request
{
  double x;
  double y;
  double z;
  double w;
} arm_interface_pkg__srv__QuaternionToEuler_Request;

// Struct for a sequence of arm_interface_pkg__srv__QuaternionToEuler_Request.
typedef struct arm_interface_pkg__srv__QuaternionToEuler_Request__Sequence
{
  arm_interface_pkg__srv__QuaternionToEuler_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} arm_interface_pkg__srv__QuaternionToEuler_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/QuaternionToEuler in the package arm_interface_pkg.
typedef struct arm_interface_pkg__srv__QuaternionToEuler_Response
{
  /// response
  double roll;
  double pitch;
  double yaw;
} arm_interface_pkg__srv__QuaternionToEuler_Response;

// Struct for a sequence of arm_interface_pkg__srv__QuaternionToEuler_Response.
typedef struct arm_interface_pkg__srv__QuaternionToEuler_Response__Sequence
{
  arm_interface_pkg__srv__QuaternionToEuler_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} arm_interface_pkg__srv__QuaternionToEuler_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ARM_INTERFACE_PKG__SRV__DETAIL__QUATERNION_TO_EULER__STRUCT_H_
