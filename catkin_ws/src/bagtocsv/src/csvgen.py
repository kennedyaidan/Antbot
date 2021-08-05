#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#you must first specify the following variables: 1. path, 2. joy_csv_path, 3. bag_file, 4. csv file name, 5. topic name for each topic
#this program can generate up to two topics into csv's


import csv
import os
import cv2
import rosbag
import sys
import argparse
import Tkinter
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from PIL import Image
from datetime import datetime
from tf.transformations import euler_from_quaternion, quaternion_from_euler
#path is for path to where the bag file is located. joy_csv_path is where csv will be written
#bag_file is the file name of the bag you want to generate a csv for
path = "/home/smerc/Desktop/smart_grids_garrett/rosbag"
os.chdir(path)
retval = os.getcwd()
bag_file = '2020-11-20-10-18-11.bag'
topic_name = '/left/feedback'
joy_csv_path = "/home/smerc/Desktop/smart_grids_garrett/rosbag"
bag = rosbag.Bag(bag_file, 'r')
bridge = CvBridge()
sysarg = sys.argv
#specify output csv file name in the "with open" command for each topic.  Also specify topic names
header_counter = 1
for topic, msg, time in bag.read_messages(topics=[topic_name]):
    timestr = str(datetime.fromtimestamp(
        time.to_time()).strftime('%Y/%m/%d/%H:%M:%S.%f'))
    axes0 = str(float(msg.measured_position))
    axes1 = str(float(msg.measured_velocity))
    axes2 = str(float(msg.commanded_velocity))
    os.chdir(joy_csv_path)
    with open('left_motor6.csv', 'a+') as csvfile:
        fieldnames = ['time', 'measured_position', 'measured_velocity', 'commanded_velocity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if str(header_counter) == "1":
            writer.writeheader()
        writer.writerow(
            {'time': timestr + "\n", 'measured_position': axes0 + "\n", 'measured_velocity': axes1+"\n", 'commanded_velocity': axes2+"\n"})
        header_counter = header_counter + 1

topic_name_two = '/right/feedback'
header_counter = 1
for topic, msg, time in bag.read_messages(topics=[topic_name_two]):
    timestr = str(datetime.fromtimestamp(
        time.to_time()).strftime('%Y/%m/%d/%H:%M:%S.%f'))
    axes0 = str(float(msg.measured_position))
    axes1 = str(float(msg.measured_velocity))
    axes2 = str(float(msg.commanded_velocity))
    os.chdir(joy_csv_path)
    with open('right_motor6.csv', 'a+') as csvfile:
        fieldnames = ['time', 'measured_position', 'measured_velocity', 'commanded_velocity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if str(header_counter) == "1":
            writer.writeheader()
        writer.writerow(
            {'time': timestr + "\n", 'measured_position': axes0 + "\n", 'measured_velocity': axes1+"\n", 'commanded_velocity': axes2+"\n"})
        header_counter = header_counter + 1
