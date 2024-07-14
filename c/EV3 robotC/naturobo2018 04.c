
task main()
{
	while(true)
	{
		if(SensorValue[S4]==1)
		{
			motor[motorB]=50;
			motor[motorC]=-50;
		}
		else if(SensorValue[S2]==1)
		{
			motor[motorB]=50;
			motor[motorC]=-50;
		}
		else
		{
			motor[motorB]=0;
			motor[motorC]=0;
		}
	}
}
