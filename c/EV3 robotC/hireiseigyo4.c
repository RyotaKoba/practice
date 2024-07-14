
task main()
{
 nMotorEncoder[motorA] = 0;
 nMotorEncoder[motorB] = 0;
 float y = 75,x,a=-160,b;
 while(true)
 {
   x = y - nMotorEncoder[motorA];
   b = a - nMotorEncoder[motorB];
   motor[motorA] = 0.2*x;
   motor[motorB] = 0.3*b +0.2*(x);
   displayBigTextLine(1,"b = %d",b);
   displayBigTextLine(3,"x = %d",x);
}
}
