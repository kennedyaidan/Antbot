#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


## Signal_strength that publishes std_msgs/String messages about the
## dBm (deciBels per milliwatt, a common measure of wifi signal strength)
## at a constant rate to the 'signal_strength' topic.

import time
import rospy
from std_msgs.msg import String
import sys
import subprocess, select
import os 
import signal

##change these
interface = "wlan1"

def execute(cmd):
        my_env = os.environ.copy()
        proc = subprocess.Popen(cmd, bufsize=20, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, env=my_env)
        for stdout_line in iter(proc.stderr.readline, ""):
           yield stdout_line 
        proc.stdout.close()

if __name__ == '__main__':
    pub = rospy.Publisher('signal_strength', String, queue_size=1)
    rospy.init_node('signal_strength', anonymous=True)
    signal_list = []
    sig_value = []
    sig_name = []
    counter = 0
    array_counter = 0 

    for path in execute(['sudo','airodump-ng', interface]):
        strength = path.find("  -")+2
        #print(path[strength+1:strength+3])
        #print(path[name:name+13])
        # Create a signal list for 50 values
        if ("UCLA_" in path) and (int(path[strength+1:strength+3]) < 100) and (int(path[strength+1:strength+3]) > 30) and counter <= 100:
            name = path.find("UCLA")
            signal_list.append(path[name:name+13]) if path[name:name+13] not in signal_list else signal_list
            counter = counter + 1   
        # When signal list is finished, make a strength array the size of the signal list
        if counter == 100:
            signal_strength = [0]*len(signal_list)
            print(signal_list)
            print("list completed!")
            counter = counter +1
        # Make a signal strength array  
        if ("UCLA_" in path) and counter > 100:
            name = path.find("UCLA")
            # Collect some signal values
            if array_counter <= 20:
                sig_name.append(path[name:name+13])
                sig_value.append(path[strength+1:strength+3])
                array_counter = array_counter + 1 
            # Organize the values in a readable array    
            else:  
                for a in range(len(signal_list)):
                     for b in range(len(sig_name)):
                           if sig_name[b] == signal_list[a]:
                                  signal_strength[a] = sig_value[b]
                rospy.loginfo(str(signal_strength))
                # Publishes signal_strength for rosbag
                pub.publish(str(signal_strength))
                # Reset arrays and lists
                array_counter = 0 
                #signal_strength = [0]*len(signal_list)
                sig_name = []
                sig_value = []
        
       
