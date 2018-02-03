import sys
import rosbag
from rospy_message_converter import message_converter
from rospy.numpy_msg import numpy_msg       
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np


#Currently just find the nearest neighbour within each frame, could later change to linear interpolator or nearest neighbour.
def interpolate(msg,joints,ind):
    nsec = msg.header.stamp.nsecs
    positions = joints[ind]
    argmin  = positions[0]
    mingap  = argmin.header.stamp.nsecs-nsec
    mingap = max(mingap,-mingap)
    for j in positions:
        gap = j.header.stamp.nsecs-nsec
        gap = max(gap,-gap)
        if gap < mingap:
            mingap = gap
            argmin = j
    img =  bridge.imgmsg_to_cv2(msg,"bgr8")
    return [img,argmin.position,argmin.velocity,argmin.effort]

if __name__=="__main__":
    imageName = sys.argv[1]
    jointName = sys.argv[2]
    saveName = sys.argv[3]
    imageBag = rosbag.Bag(imageName)
    jointBag = rosbag.Bat(jointName)
    bridge = CvBridge()
    cur = 0
    joints = []
    data = []
    for topic,msg,t in bag.read_messages(topics=['robot/joint_states']):
         sectime = msg.header.stamp.secs
         if sectime > cur
            cur = sectime
            joints.append([msg])
         else:
             joints[-1].append(msg)
    firstT = joints[0][0].header.stamp.secs
    for topic, msg, t in bag.read_messages(topics=['image_raw']):
        time = msg.header.stamp.secs
        ind = time-firstT
        if ind>=0:            
            data.append(interpolate(msg,joints,ind))
    np.savez_compressed(data,d=data)
    imageBag.close()
    jointBag.close()
