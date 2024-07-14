
task main()
{
	int i=SensorValue[S1];
while(true)
{
if(SensorValue[S2]<20)
{
	while(i<90)
	{
		i=SensorValue[S1];
		motor[motorB]=92-i;
		motor[motorC]=-92+i;
	}
	resetGyro(S1);
}
	else
	{
		motor[motorB]=50;
		motor[motorC]=50;
	}
}
}
