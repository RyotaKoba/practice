void motor_go();
void motor_turn(int n);

task main()
{
	while(true)
	{
		motor_go();
		motor_turn(300);
	}
}

void motor_go()
{
	motor[motorB]=50;
	motor[motorC]=50;
	wait1Msec(1000);
}

void motor_turn(int n)
{
	nMotorEncoder[motorB] = 0;
	nMotorEncoder[motorC] = 0;
	while((nMotorEncoder[motorB] < n)||(nMotorEncoder[motorC] > -n))
	{
		motor[motorB] = 20;
		motor[motorC] = -20;
	}
}
