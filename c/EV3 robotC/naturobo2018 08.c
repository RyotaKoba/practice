void motor_turn();
void motor_go();

task main()
{
	motor_turn();
	motor_go();


}

void motor_go()
{
	motor[motorB]=50;
	motor[motorC]=50;
	wait1Msec(2000);
}

void motor_turn()
{
	motor[motorB]=50;
	motor[motorC]=0;
	wait1Msec(1500);
}
