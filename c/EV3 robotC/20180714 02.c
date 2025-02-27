#pragma config(Sensor, S1,     ,               sensorEV3_Gyro)
#pragma config(Sensor, S2,     ,               sensorEV3_Ultrasonic)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

task main()
{
	resetGyro(S1);

	int i = SensorValue[S1],u = SensorValue[S2];
	while(true)
	{
		u = SensorValue[S2];
		resetGyro(S1);
		wait1Msec(1000);
   while(u<10)
   {
     u = SensorValue[S2];
     i = SensorValue[S1];
     motor[motorB]=30-i;
     motor[motorC]=30+i;
   }
   motor[motorB]=10;
   motor[motorC]=10;
   wait1Msec(1500);
   motor[motorB]=0;
   motor[motorC]=0;
   wait1Msec(500);
   while(i<90)
		{
		i=SensorValue[S1];
			motor[motorB]=(90-i);
			motor[motorC]=-(90-i);
			}
   motor[motorB]=20;
   motor[motorC]=20;
   wait1Msec(3000);

   resetGyro(S1);
 }
}
