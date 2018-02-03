import sys
import rosbag
from rospy_message_converter import message_converter
from rospy.numpy_msg import numpy_msg       
import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np




if __name__=="__main__":
    bagname = sys.argv[1]
    savename = sys.argv[2]
    bag = rosbag.Bag(bagname)
    bridge = CvBridge()
    frames = []
    i = 1
    for topic, msg, t in bag.read_messages(topics=['image_raw']):
        if i<10:
            print msg.header.stamp.secs, msg.header.stamp.nsecs
        i+=1
        img = bridge.imgmsg_to_cv2(msg,"bgr8")
        frames.append([t,img])
        # cv2.imshow("pic.png", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        #print(dictionary['position'][5])
    np.savez_compressed(savename,img=frames)
    bag.close()

