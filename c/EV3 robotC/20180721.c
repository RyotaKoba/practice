
task main()
{
	resetGyro(S1);

	int i = SensorValue[S1],u = SensorValue[S2],t = SensorValue[S4];
	while(true)
	{
		t = SensorValue[S4];
		resetGyro(S1);
		wait1Msec(1000);
   while(t==0)
   {
     t = SensorValue[S4];
     i = SensorValue[S1];
     motor[motorB]=30-i;
     motor[motorC]=30+i;
   }
   u =SensorValue[S2];
   motor[motorB]=0;
   motor[motorC]=0;
   wait1Msec(500);

   if(u<15)
   {
     while(i>-90)
		{
		i=SensorValue[S1];
			motor[motorB]=-(90+i);
			motor[motorC]=(90+i);
			}
   resetGyro(S1);
 }else{
   while(i<90)
		{
		i=SensorValue[S1];
			motor[motorB]=(90-i)+1;
			motor[motorC]=-(90-i)-1;
			}
   resetGyro(S1);
 }
}

}
