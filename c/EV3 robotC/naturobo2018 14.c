void motor_go();
void motor_turn(int n);

task main()
{
	while(true)
	{
		motor_go();
		motor_turn(393); //���O�p�
	}                  //�����`
}                    //���܊p�
                     //���Z�p�
void motor_go()      //�����p�
{                    //��	39
	motor[motorB]=50;
	motor[motorC]=50;
	wait1Msec(1500);
	motor[motorB]=0;
	motor[motorC]=0;
	wait1Msec(500);
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
motor[motorB]=0;
motor[motorC]=0;
wait1Msec(500);
}
