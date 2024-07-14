void motor_go(int p,int t);

task main()
{
 while(true)
 {
   motor_go(50,3000);
   motor_go(-30,2000);
}
}

void motor_go(int p,int t)
{
	motor[motorB]=p;
	motor[motorC]=p;
	wait1Msec(t);
}
