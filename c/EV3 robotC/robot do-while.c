
task main()
{
	int i = 0;
	do
	{
		motor[motorB] = -30;
		motor[motorC] = -50;
		wait1Msec(1500);

    motor[motorB] = 50;
    motor[motorC] = 0;
    wait1Msec(1000);

    i++;
  }while (i < 3);
}
