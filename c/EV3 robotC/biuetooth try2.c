#include "ev3 id.h"

task main()
{
  int data=0;

  while(true)
{
	data = RecieveBTMsg();
	ev3DisplayCenteredTextLine(3,"Recieve %2d",data);
	wait1Msec(100);
}
}
