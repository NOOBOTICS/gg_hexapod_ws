#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>
#include <geometry_msgs/msg/pose_stamped.hpp>
#include <memory>

void move_robot(const std::shared_ptr<rclcpp::Node> node)
{
    auto leg_move_group = moveit::planning_interface::MoveGroupInterface(node, "gg_hex_leg");

    // Define the pose goal (position and orientation)
    geometry_msgs::msg::PoseStamped pose_goal;
    
    pose_goal.header.frame_id = "world";  // Adjust to your robot's reference frame
    pose_goal.pose.position.x = 0.20427;        // Updated x position
    pose_goal.pose.position.y = -0.0034262;     // Updated y position
    pose_goal.pose.position.z = 0.20501;        // Updated z position
    
    // Define the orientation as a quaternion
    pose_goal.pose.orientation.x = 0.70689;    // Updated orientation x
    pose_goal.pose.orientation.y = -0.017336;  // Updated orientation y
    pose_goal.pose.orientation.z = 0.0054816;  // Updated orientation z
    pose_goal.pose.orientation.w = 0.70709;    // Updated orientation w

    // Set the pose target for the move group
    leg_move_group.setPoseTarget(pose_goal);

    // Plan and execute the motion
    moveit::planning_interface::MoveGroupInterface::Plan gg_hex_plan;

    bool plan_success = (leg_move_group.plan(gg_hex_plan) == moveit::core::MoveItErrorCode::SUCCESS);

    if(plan_success)
    {
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
                    "Planner SUCCEED, moving the leg");
        leg_move_group.move();
    }
    else
    {
        RCLCPP_ERROR(rclcpp::get_logger("rclcpp"),
                     "One or more planners failed!");
        return;
    }
}

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("simple_moveit_interface");
    move_robot(node);

    rclcpp::spin(node);
    rclcpp::shutdown();
}
