
task A()
{
    motor[motorA] = 20;
    wait1Msec(1000);
    motor[motorA] = 0;
}

task main()
{
   startTask(A);
   wait1Msec(200);
}
