
task main()
{
	int flag =0;
	while(flag<5)
	{
		flag++;
		motor[motorB]=30;
		motor[motorC]=30;
		wait1Msec(500);
		if(flag==1)
		{
			displayBigTextLine(1,"(1,0)");
		}
		if(flag==2)
		{
			displayBigTextLine(1,"(2,0)");
			motor[motorB]=20;
			motor[motorC]=-20;
			wait1Msec(1200);
		}
		if(flag==3)
		{
			displayBigTextLine(1,"(2,1)");
		}
		if(flag==4)
		{
			displayBigTextLine(1,"(2,2)");
		}
	}
}
