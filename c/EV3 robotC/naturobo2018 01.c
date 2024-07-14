
task main()
{
	while(SensorValue[S4]==0)
	{
		motor[motorB] = 50;
		motor[motorC] = 50;
	}
	motor[motorB]=-50;
	motor[motorC]=-50;
	wait1Msec(1000);
}
