
task main()
{
	while(true)
	{
		if(SensorValue[S4]==0)
		{
			motor[motorB]=50;
			motor[motorC] =50;
		}
		else
		{
			motor[motorB]=50;
			motor[motorC]=-50;
		}
	}
}
