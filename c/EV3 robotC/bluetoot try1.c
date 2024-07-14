#include "ev3 id.h"

task main()
{
  int i;

  CheckBT(SLAVE2)
  for(i=1;i<=10;i++)
  {SendBTMsg(SLAVE2, i);
  	ev3DisplayCenteredTextLine(2,"Sending %2d",i);
  	wait1Msec(1000);

  	if(i >= 10) i = 0;
  }
}
