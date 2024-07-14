
task main()
{
 int i=0;

 while(i<=40)
 {
   i++;
   motor[motorB]=i;
   motor[motorC]=i;
   wait1Msec(100);
 }
 motor[motorB]=i;
 motor[motorC]=i;
 wait1Msec(2000);
 while(i>0)
 {
	i--;
motor[motorB]=i;
motor[motorC]=i;
wait1Msec(50);
}
}
