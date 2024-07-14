
task main()
{
 while(true)
 {
   if(SensorValue[S2] == 1)
   {
     motor[motorA] = 100;
     motor[motorD] = -100;
     motor[motorB] = 0;
     wait1Msec(100);
     motor[motorA] = 100;
     motor[motorD] = -100;
     motor[motorB] = 100;
     wait1Msec(1000);
   }
 }
}
