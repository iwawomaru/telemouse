import rospy

from audio_disconf import AudioDisconf
from esn import ESN


obj_0 = AudioDisconf(node_name="breathe_left_node", 
                   esn_pickle="esn_breathe_left.pickle",
                   acc_t=2.0, disconf_t=0.6, decay=0.6)

obj_1 = AudioDisconf(node_name="breathe_right_node", 
                   esn_pickle="esn_breathe_right.pickle",
                   acc_t=2.0, disconf_t=0.6, decay=0.6)

obj_2 = AudioDisconf(node_name="pick_left_node", 
                   esn_pickle="esn_pick_left.pickle",
                   acc_t=2.0, disconf_t=0.6, decay=0.6)

obj_3 = AudioDisconf(node_name="pick_right_node", 
                   esn_pickle="esn_pick_right.pickle",
                   acc_t=2.0, disconf_t=0.6, decay=0.6)

obj_4 = AudioDisconf(node_name="loud_left_node", 
                   esn_pickle="esn_loud_left.pickle",
                   acc_t=2.0, disconf_t=0.6, decay=0.6)

obj_5 = AudioDisconf(node_name="loud_right_node", 
                   esn_pickle="esn_loud_right.pickle",
                   acc_t=2.0, disconf_t=0.6, decay=0.6)

rospy.spin()
