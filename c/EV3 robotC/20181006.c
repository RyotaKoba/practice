void motor_encoder(int p);
void Stop_motor(void);
void right_turn(void);
void left_turn(void);
void reset(void);
task main()
{
	int beg_w=0,beg_h=0;
	while(beg_h<1080)
	{
		reset();
		motor_encoder(360);
		beg_h=beg_h+nMotorEncoder[motorB];
		displayBigTextLine(1,"beg_h:%d",beg_h);
		Stop_motor();
		if(beg_w<720)
		{
			right_turn();
			reset();
			motor_encoder(360);
			beg_w=beg_w+nMotorEncoder[motorB];
			displayBigTextLine(4,"beg_w:%d",beg_w);
			Stop_motor();
		}
		left_turn();
	}
	reset();
	while(nMotorEncoder[motorB]<beg_w)
	{
		motor[motorB]=50;
		motor[motorC]=50;
	}
	left_turn();
	reset();
	while(nMotorEncoder[motorB]<beg_h)
	{
		motor[motorB]=50;
		motor[motorC]=50;
	}
}
void motor_encoder(int p)
{
	while(nMotorEncoder[motorB]<p)
	{
		motor[motorB]=50;
		motor[motorC]=50;
	}
}
void Stop_motor()
{
	motor[motorB] = 0;
	motor[motorC] = 0;
	wait1Msec(1000);
}
void right_turn()
{
	motor[motorB]=-20;
	motor[motorC]=20;
	wait1Msec(1100);
}
void left_turn()
{
	motor[motorB]=20;
	motor[motorC]=-20;
	wait1Msec(1100);
}
void reset()
{
	nMotorEncoder[motorB]=0;
}
