void go_straight()
{
	nMotorEncoder[motorB] = 0;

	motor[motorB] = 50;
	motor[motorC] = 50;
	while (nMotorEncoder[motorB] < 90)
	{
		// wait
	}
	motor[motorB] = 0;
	motor[motorC] = 0;
}

task main()
{
	go_straight();
}
