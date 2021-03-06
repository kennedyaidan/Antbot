#include <sys/stat.h>
#include <fcntl.h>

#include <ros/ros.h>
#include <sensor_msgs/Range.h>

int main( int argc, char **argv)
{

  ros::init( argc, argv, "publish_sonar");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<sensor_msgs::Range>("sonar0", 1);
  sensor_msgs::Range rangeMsg;
  char rxBuf[80];
  float range;
  int fd;
  fd = open("/dev/ttyUSB0", O_EXCL);
  if (fd < 0)
    {
      std::cerr << "Error opening sonar tty\n";
      return(-1);
    }

  while(ros::ok())

    {

      // Maxbotix output is R1234, range in mm
      int i = 0;
      while(read(fd, &rxBuf[i], 1)) {
	if (rxBuf[i] == '\n') {
	  rxBuf[i] = '\0';
	  break;
	}
	i++;
      }
      
      range = strtof(&rxBuf[1], NULL) / 1000; // output in meters
      ROS_INFO("Range: %.5f", strtof(&rxBuf[1], NULL));
      rangeMsg.range = range;
      rangeMsg.header.stamp = ros::Time::now();
      pub.publish(rangeMsg);
      if(range <= 0.007)
	ROS_INFO("STOPPPPP: %.4f", range);
    }
  return(0);

}
