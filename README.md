# Anbot is a 4WD mobile robot capable of SLAM and Autonomous Navigation. The hardware and software was initially developed several years ago as part of pilot program for mobile battery energy storage within UCLA's SMERC Lab (http://smartgrid.ucla.edu/CAEV/). The program was initally called trog, which is a play on the word trogolodyte. I picked up this vehicle as my capstone project in my Master's program to explore the fields of SLAM and Autonomous Navigation.


# Documentation
My capstone project for this repository can be found here: kennedyaidan/Antbot/Masters_Project.pdf
- 



# SLAM
SLAM can be performed with:
- Cartographer (default)
- GMapping


# Autonomous Navigation
Navigation of uknown and known maps can be performed with:
- DWA
- TEB


# Components
This is an overview of the key components of Antbot:
- Velodyne VLP-16 LiDAR
- Jetson TX2 Developer Kit
- RoboteQ SDC2130 - 2x20A 30V Motor Controller with Encoder Input
- Samsung 850 EVO 250GB 2.5-Inch SATA III Internal SSD
- 24V LiFeMnPO4 Prismatic Battery 100Ah
- Superdroid IG52-DB4, 4WD All Terrain Heavy Duty Robot Platform 


# Gazebo interface
For convient software development, a full Gazebo model of Antbot can used, it includes:
- VLP-16 LiDAR simulator
- 4WD differtial drive controlled wheels


