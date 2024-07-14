
task main()
{
 int i = SensorValue[S1],a=1;
 while(true)
 {
		motor[motorB]=50;
		motor[motorC]=50;
		wait1Msec(1000);
		while(i<=a*90)
		{
		i=SensorValue[S1];
			motor[motorB]=10;
			motor[motorC]=-10;
			}
			a++;
}
}
