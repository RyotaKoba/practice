
task main()
{
 nMotorEncoder[motorA] = 0;
 nMotorEncoder[motorB] = 0;
 float y = -75,x,a=160,b;
 int flag = 0;
 while(true)
 {
   x = y - nMotorEncoder[motorA];
   b = a - nMotorEncoder[motorB];
   motor[motorA] = 0.2*x;
   motor[motorB] = 0.3*b +0.2*(x);
   wait1Msec(800)
   flag == 1;
   flag = 1;
   motor[motorA] = 0;
   motor[motorB] = 0;
   wait1Msec(2000)
}
}
