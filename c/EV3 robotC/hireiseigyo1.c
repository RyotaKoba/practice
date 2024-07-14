
task main()
{
	int x;
    while(true)
    {
    	x = nMotorEncoder[motorA];
    	motor[motorA] = -5 * x;
    	displayBigTextLine(1,"x = %d",x);
    }
}
