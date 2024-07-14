void motor_go()
{
	motor[motorB]=50;
	motor[motorC]=50;
}
task main()
{
 motor_go();
 wait1Msec(2000);
}
