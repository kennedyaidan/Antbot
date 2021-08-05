#This is working copy of "Trog" Folder (copied on 061421), updated by Aidan Kennedy




# Trog
Trog is a pilot mobile battery energy storage system that works in integration with the grid to deliver on-demand energy. Trog, or Troggie, is part of [CAEV](http://smartgrid.ucla.edu/CAEV/). Troggie's name is a play on the word troglodyte (i.e. a person who lived in a cave). 

Troggie is pictured [here](documentation/images/troggie.png). A demonstration video can be seen [here](https://www.youtube.com/watch?v=KBPcC1sAmNI&feature=youtu.be)



# ToDo List
========
#### Software
* [ ] Calibrate IMU and fuse with odometry
* [ ] Get GPS readings

#### Hardware
* [ ] Get Touch Screen Monitor






# What can Troggie Do?
========
Currently, Troggie is capable of indoor and outdoor navigation. Troggie can navigate autonomously ***within known maps***. 
Meaning, in order to begin autonomous navigation, a map must first be made. Please refer to [trog_bringup](./ros/src/trog_bringup)
for more detailed instructions. 

# Components
========
This is an overview of the key components of Troggie:

- Velodyne VLP-16 LiDAR
- Jetson TX2 Developer Kit
- RoboteQ SDC2130 - 2x20A 30V Motor Controller with Encoder Input
- Samsung 850 EVO 250GB 2.5-Inch SATA III Internal SSD
- 24V LiFeMnPO4 Prismatic Battery 100Ah
- Superdroid IG52-DB4, 4WD All Terrain Heavy Duty Robot Platform (with customized upper deck)
- N/A: SparkFun 9DoF Razor IMU M0
- N/A: Garmin 18x GPS



# Open Issues
========
- Velodyne Lidar: Packet containing angle overflow
	Open issue: https://github.com/ros-drivers/velodyne/issues/275
	It is a continuous error which prints out to the console every 60s 
	Uncertain what effect this has on Lidar performance
- Parameter max_trans_vel is deprecated (and will not load properly). Use max_vel_trans_instead

