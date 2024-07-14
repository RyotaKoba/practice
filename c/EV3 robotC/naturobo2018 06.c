void motor_go();

task main()
{
 motor_go();
wait1Msec(2000);
}

void motor_go()
{
	motor[motorB]=50;
	motor[motorC]=50;
}
