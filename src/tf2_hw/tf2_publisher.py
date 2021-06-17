#! /usr/bin/python3
#import the rospy package 
import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import euler_from_quaternion
import math
import tf2_ros
import turtlesim.srv

rospy.init_node("mynode")
tf_buffer = tf2_ros.Buffer()


def callback(data):
    goal = PoseStamped()

    goal.header.seq = 1
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"

    goal.pose.position.x = 1.0
    goal.pose.position.y = 2.0
    goal.pose.position.z = 0.0

    # quaternion = euler_from_quaternion(0, 0, -math.radians(wp[0].transform.rotation.yaw))
    # goal.pose.orientation.x = quaternion[0]
    # goal.pose.orientation.y = quaternion[1]
    # goal.pose.orientation.z = quaternion[2]
    # goal.pose.orientation.w = quaternion[3]
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0

    publisher.publish(goal)

    

publisher = rospy.Publisher('/turtle2/pose_stamped', PoseStamped, queue_size=5)
#subscriber =rospy.Subscriber("turtle1/pose", PoseStamped,callback)
rate = rospy.Rate(10.0)
while not rospy.is_shutdown(): 
    try:
        trans = tf_buffer.lookup_transform('turtle2', 'turtle1', rospy.Time())
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
        rate.sleep()
        continue







# import rospy
# from std_msgs.msg import String
# #function to publish messages at the rate of 2 messages per second
# def messagePublisher():
#      #define a topic to which the messages will be published
#      message_publisher = rospy.Publisher(‘messageTopic’, String, queue_size=10)
#     #initialize the Publisher node. 
#     #Setting anonymous=True will append random integers at the end of our publisher node
#     rospy.init_node(‘messagePubNode’, anonymous=True)
#     #publishes at a rate of 2 messages per second
#     rate = rospy.Rate(2)
#     #Keep publishing the messages until the user interrupts 
#     while not rospy.is_shutdown():
#     message = “ROS Tutorial by Arsalan”
#     #display the message on the terminal
#     rospy.loginfo(‘Published: ‘ + message)
#     #publish the message to the topic
#     message_publisher.publish(message)
#     #rate.sleep() will wait enough until the node publishes the     message to the topic
#     rate.sleep()
# if __name__ == ‘__main__’:
#     try:
#         messagePublisher()
#     #capture the Interrupt signals
#     except rospy.ROSInterruptException:
#         pass