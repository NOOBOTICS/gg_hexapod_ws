// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from arm_interface_pkg:srv/QuaternionToEuler.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACE_PKG__SRV__DETAIL__QUATERNION_TO_EULER__BUILDER_HPP_
#define ARM_INTERFACE_PKG__SRV__DETAIL__QUATERNION_TO_EULER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "arm_interface_pkg/srv/detail/quaternion_to_euler__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace arm_interface_pkg
{

namespace srv
{

namespace builder
{

class Init_QuaternionToEuler_Request_w
{
public:
  explicit Init_QuaternionToEuler_Request_w(::arm_interface_pkg::srv::QuaternionToEuler_Request & msg)
  : msg_(msg)
  {}
  ::arm_interface_pkg::srv::QuaternionToEuler_Request w(::arm_interface_pkg::srv::QuaternionToEuler_Request::_w_type arg)
  {
    msg_.w = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interface_pkg::srv::QuaternionToEuler_Request msg_;
};

class Init_QuaternionToEuler_Request_z
{
public:
  explicit Init_QuaternionToEuler_Request_z(::arm_interface_pkg::srv::QuaternionToEuler_Request & msg)
  : msg_(msg)
  {}
  Init_QuaternionToEuler_Request_w z(::arm_interface_pkg::srv::QuaternionToEuler_Request::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_QuaternionToEuler_Request_w(msg_);
  }

private:
  ::arm_interface_pkg::srv::QuaternionToEuler_Request msg_;
};

class Init_QuaternionToEuler_Request_y
{
public:
  explicit Init_QuaternionToEuler_Request_y(::arm_interface_pkg::srv::QuaternionToEuler_Request & msg)
  : msg_(msg)
  {}
  Init_QuaternionToEuler_Request_z y(::arm_interface_pkg::srv::QuaternionToEuler_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_QuaternionToEuler_Request_z(msg_);
  }

private:
  ::arm_interface_pkg::srv::QuaternionToEuler_Request msg_;
};

class Init_QuaternionToEuler_Request_x
{
public:
  Init_QuaternionToEuler_Request_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_QuaternionToEuler_Request_y x(::arm_interface_pkg::srv::QuaternionToEuler_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_QuaternionToEuler_Request_y(msg_);
  }

private:
  ::arm_interface_pkg::srv::QuaternionToEuler_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interface_pkg::srv::QuaternionToEuler_Request>()
{
  return arm_interface_pkg::srv::builder::Init_QuaternionToEuler_Request_x();
}

}  // namespace arm_interface_pkg


namespace arm_interface_pkg
{

namespace srv
{

namespace builder
{

class Init_QuaternionToEuler_Response_yaw
{
public:
  explicit Init_QuaternionToEuler_Response_yaw(::arm_interface_pkg::srv::QuaternionToEuler_Response & msg)
  : msg_(msg)
  {}
  ::arm_interface_pkg::srv::QuaternionToEuler_Response yaw(::arm_interface_pkg::srv::QuaternionToEuler_Response::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interface_pkg::srv::QuaternionToEuler_Response msg_;
};

class Init_QuaternionToEuler_Response_pitch
{
public:
  explicit Init_QuaternionToEuler_Response_pitch(::arm_interface_pkg::srv::QuaternionToEuler_Response & msg)
  : msg_(msg)
  {}
  Init_QuaternionToEuler_Response_yaw pitch(::arm_interface_pkg::srv::QuaternionToEuler_Response::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_QuaternionToEuler_Response_yaw(msg_);
  }

private:
  ::arm_interface_pkg::srv::QuaternionToEuler_Response msg_;
};

class Init_QuaternionToEuler_Response_roll
{
public:
  Init_QuaternionToEuler_Response_roll()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_QuaternionToEuler_Response_pitch roll(::arm_interface_pkg::srv::QuaternionToEuler_Response::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_QuaternionToEuler_Response_pitch(msg_);
  }

private:
  ::arm_interface_pkg::srv::QuaternionToEuler_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interface_pkg::srv::QuaternionToEuler_Response>()
{
  return arm_interface_pkg::srv::builder::Init_QuaternionToEuler_Response_roll();
}

}  // namespace arm_interface_pkg

#endif  // ARM_INTERFACE_PKG__SRV__DETAIL__QUATERNION_TO_EULER__BUILDER_HPP_
