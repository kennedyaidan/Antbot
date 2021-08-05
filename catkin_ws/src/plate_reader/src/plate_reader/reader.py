#!/usr/bin/env python
import os
import sys
import time
import datetime

import rospy
import requests
import cv2
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from sensor_msgs.msg import Image as ImageMsg
import numpy as np
from PIL import Image

from db import Db

#db = Db()
image_pub = rospy.Publisher('VideoRaw', ImageMsg, queue_size=10)

def read_plate(event):
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
    _,img = cap.read()
    t = int(time.time())
    save_dir = '/home/nvidia/data/{}'.format(datetime.datetime.now().strftime("%Y-%m-%d"))
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

#    rospy.loginfo('WARNING: Not saving')
    cv2.imwrite(os.path.join(save_dir, 'plate_{}.jpg'.format(t)), img)

    # Publish image
    image_pub.publish(CvBridge().cv2_to_imgmsg(img))

    time.sleep(1)
#    with open('{}/plate_{}.jpg'.format(save_dir, t), 'rb') as f:
        # response = requests.post(
        #     'https://platerecognizer.com/plate-reader/',
        #     files=dict(upload=f),
        #     headers={'Authorization': 'Token ' + '6aa8435106c4ce07b0d2608f1057f2fee9630f37'})
    # try:
    #     plate_seq = response.json()['results'][0]['plate']
    # except KeyError:
    #     return
    # except IndexError:
    #     returnfrom sensor_msgs.msg import Image

 #   rospy.loginfo('Read plate: {}'.format(plate_seq))

    # Add to db
    #db.add_plate(plate_seq)



if __name__ == '__main__':
    rospy.init_node('reader')

    # Executes callback on publish event
    # rospy.Subscriber('/read_plate', String, read_plate)

    # Executes callback every X seconds
    rospy.Timer(rospy.Duration(1), read_plate)

    rospy.loginfo('Starting plate reader node...')
    rospy.spin()
