task main()
{
  int i = 0;
  while (i < 5)
  {
  	motor[motorB] = 50;
  	motor[motorC] = 50;
  	wait1Msec(1000);

  	motor[motorB] = 50;
  	motor[motorC] = 0;
  	wait1Msec(1800);

  	i++;
  }
}
