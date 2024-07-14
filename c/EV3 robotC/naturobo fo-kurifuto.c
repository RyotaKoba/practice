
task main()
{
  motor[motorB] = -50;
  motor[motorD] = -50;
  wait1Msec(5000);

  motor[motorB] = 0;
  motor[motorD] = 0;
  motor[motorA] = 50;
  wait1Msec(10000);
}
