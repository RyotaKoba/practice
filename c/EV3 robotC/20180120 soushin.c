[sourcecode language="cpp" wraplines="false" collapse="false"]

task main()
{
 wait1Msec(500);

 int number_1=5;
 int number_2=-1;
 int number_3=700;
 sendMessageWithParm(number_1,number_2,number_3);
 wait1Msec(3000);
 number_1=2;
 number_2=4;
 number_3=6;
 sendMessageWithParm(number_1,number_2,number_3);

}
