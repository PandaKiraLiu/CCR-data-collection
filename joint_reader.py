import sys
import rosbag
from rospy_message_converter import message_converter
from rospy.numpy_msg import numpy_msg       
import numpy as np

#Sample joint_state message
"""
secs: 1517286151
nsecs: 709962965
frame_id: ''
name: ['head_pan', 'right_j0', 'right_j1', 'right_j2', 'right_j3', 'right_j4', 'right_j5', 'right_j6', 'torso_t0']
position: [-0.7621279296875, 0.7418427734375, -1.063486328125, -0.7452353515625, 1.5070849609375, -0.388291015625, 0.4973642578125, 3.8773544921875, 0.0]
velocity: [-0.001, -0.001, -0.001, -0.001, -0.001, -0.001, -0.001, -0.001, 0.0]
effort: [0.0, 0.104, -18.584, -6.496, -11.076, 2.068, -0.252, 0.24, 0.0]
"""



if __name__=="__main__":
    bagname = sys.argv[1]
    savename = sys.argv[2]
    bag = rosbag.Bag(bagname)
    positions = []
    velocities = []
    efforts = []
    i=0
    for topic, msg, t in bag.read_messages(topics=['/robot/joint_states']):    
        if i<10:
            print msg.header.stamp.secs, msg.header.stamp.nsecs
            # print t
            i+=1
        else:
            break
        positions.append([t,msg.position])
        velocities.append([t,msg.velocity])
        efforts.append([t,msg.effort])
    np.savez_compressed(savename,p=positions,v=velocities,e=efforts)
    bag.close()

