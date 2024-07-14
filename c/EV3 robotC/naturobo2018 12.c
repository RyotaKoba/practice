void motor_go(int p,int d);

task main()
{
	while(true)
	{
		motor_go(50,1200);
		motor_go(-50,800);
	}
}

void motor_go(int p,int d)
{
	nMotorEncoder[motorB]=0;
	nMotorEncoder[motorC]=0;
	if(p>0)
	{
		while(nMotorEncoder[motorB]<d)
		{
			motor[motorB]=p;
			motor[motorC]=p;
		}
	}
	else
	{
		while(nMotorEncoder[motorB]>-d)
		{
			motor[motorB]=p;
			motor[motorC]=p;
		}
	}
}
