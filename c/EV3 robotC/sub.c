
void a()
{
	nMotorEncoder[motorB] = 0;

  motor[motorB] = 10;
	while (nMotorEncoder[motorB] < 90)
{
	//wait
}
motor[motorB] = 0;
}
void b()
{
	nMotorEncoder[motorB] = 0;
	motor[motorB] = -10;
	while (nMotorEncoder[motorB] > -90)
	{
		//wait
}
motor[motorB] = 0;
}
task main()
{
	a();
	wait10Msec(50);
	b();
	wait10Msec(100);
}
