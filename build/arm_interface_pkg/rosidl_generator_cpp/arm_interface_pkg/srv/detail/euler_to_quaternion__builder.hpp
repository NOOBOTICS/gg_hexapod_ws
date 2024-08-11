// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from arm_interface_pkg:srv/EulerToQuaternion.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACE_PKG__SRV__DETAIL__EULER_TO_QUATERNION__BUILDER_HPP_
#define ARM_INTERFACE_PKG__SRV__DETAIL__EULER_TO_QUATERNION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "arm_interface_pkg/srv/detail/euler_to_quaternion__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace arm_interface_pkg
{

namespace srv
{

namespace builder
{

class Init_EulerToQuaternion_Request_yaw
{
public:
  explicit Init_EulerToQuaternion_Request_yaw(::arm_interface_pkg::srv::EulerToQuaternion_Request & msg)
  : msg_(msg)
  {}
  ::arm_interface_pkg::srv::EulerToQuaternion_Request yaw(::arm_interface_pkg::srv::EulerToQuaternion_Request::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interface_pkg::srv::EulerToQuaternion_Request msg_;
};

class Init_EulerToQuaternion_Request_pitch
{
public:
  explicit Init_EulerToQuaternion_Request_pitch(::arm_interface_pkg::srv::EulerToQuaternion_Request & msg)
  : msg_(msg)
  {}
  Init_EulerToQuaternion_Request_yaw pitch(::arm_interface_pkg::srv::EulerToQuaternion_Request::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_EulerToQuaternion_Request_yaw(msg_);
  }

private:
  ::arm_interface_pkg::srv::EulerToQuaternion_Request msg_;
};

class Init_EulerToQuaternion_Request_roll
{
public:
  Init_EulerToQuaternion_Request_roll()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_EulerToQuaternion_Request_pitch roll(::arm_interface_pkg::srv::EulerToQuaternion_Request::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_EulerToQuaternion_Request_pitch(msg_);
  }

private:
  ::arm_interface_pkg::srv::EulerToQuaternion_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interface_pkg::srv::EulerToQuaternion_Request>()
{
  return arm_interface_pkg::srv::builder::Init_EulerToQuaternion_Request_roll();
}

}  // namespace arm_interface_pkg


namespace arm_interface_pkg
{

namespace srv
{

namespace builder
{

class Init_EulerToQuaternion_Response_w
{
public:
  explicit Init_EulerToQuaternion_Response_w(::arm_interface_pkg::srv::EulerToQuaternion_Response & msg)
  : msg_(msg)
  {}
  ::arm_interface_pkg::srv::EulerToQuaternion_Response w(::arm_interface_pkg::srv::EulerToQuaternion_Response::_w_type arg)
  {
    msg_.w = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interface_pkg::srv::EulerToQuaternion_Response msg_;
};

class Init_EulerToQuaternion_Response_z
{
public:
  explicit Init_EulerToQuaternion_Response_z(::arm_interface_pkg::srv::EulerToQuaternion_Response & msg)
  : msg_(msg)
  {}
  Init_EulerToQuaternion_Response_w z(::arm_interface_pkg::srv::EulerToQuaternion_Response::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_EulerToQuaternion_Response_w(msg_);
  }

private:
  ::arm_interface_pkg::srv::EulerToQuaternion_Response msg_;
};

class Init_EulerToQuaternion_Response_y
{
public:
  explicit Init_EulerToQuaternion_Response_y(::arm_interface_pkg::srv::EulerToQuaternion_Response & msg)
  : msg_(msg)
  {}
  Init_EulerToQuaternion_Response_z y(::arm_interface_pkg::srv::EulerToQuaternion_Response::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_EulerToQuaternion_Response_z(msg_);
  }

private:
  ::arm_interface_pkg::srv::EulerToQuaternion_Response msg_;
};

class Init_EulerToQuaternion_Response_x
{
public:
  Init_EulerToQuaternion_Response_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_EulerToQuaternion_Response_y x(::arm_interface_pkg::srv::EulerToQuaternion_Response::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_EulerToQuaternion_Response_y(msg_);
  }

private:
  ::arm_interface_pkg::srv::EulerToQuaternion_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interface_pkg::srv::EulerToQuaternion_Response>()
{
  return arm_interface_pkg::srv::builder::Init_EulerToQuaternion_Response_x();
}

}  // namespace arm_interface_pkg

#endif  // ARM_INTERFACE_PKG__SRV__DETAIL__EULER_TO_QUATERNION__BUILDER_HPP_
