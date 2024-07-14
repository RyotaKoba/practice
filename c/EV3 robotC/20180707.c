
task main()
{
 int i=0;
 while(i<=99)
 {
   i++;
   motor[motorB]=i;
   motor[motorC]=i;
   wait1Msec(50);
 }
 wait1Msec(2000);
}
