#pragma config(Sensor, S1,     L1,             sensorLightActive)
#pragma config(Sensor, S2,     L2,             sensorEV3_Color)
#pragma config(Sensor, S3,     L3,             sensorLightActive)
#pragma config(Sensor, S4,     ,               sensorEV3_Touch)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

//color
#define WHITE 0
#define BLACK 1
#define SELBER 2
//action
//light
int Left_Light(void);
int Senter_Light(void);
int Rigth_Light(void);

//motor_
void Advance_motor(void);
void Rigth_motor(void);
void Left_motor(void);
void Back_motor(void);
void Stop_motor(void);
//motor_encoder
void E_A_motor(int n);
void E_R_motor(int n);
void E_L_motor(int n);
void E_B_motor(int n);
//main
task main()
{
	int flag = 0;
	int n=0;
	int r,s,l,data;
	int rflag = 0,lflag = 0;
	data =0;
	while(SensorValue[S4]==0)
	{
		if(SensorValue[L2] <10){
			data = 0;
		}else{
			data = 1;
		}
	}
	while(true)
	{
		l=Left_Light();
		s=Senter_Light();
		r=Rigth_Light();
		if(l == SELBER){
			lflag = 1;
		}
		if(r == SELBER){
			rflag = 1;
		}
		if(l == WHITE && r == WHITE){
		 Advance_motor()}
		if(l == BLACK && r == WHITE){
		 Rigth_motor()}
		if(l == WHITE && r == BLACK){
		 Left_motor()
		 }
		if(l == BLACK && r == BLACK){
			if(lflag==1 && (!(rflag==1)) ){
				if(n == data){
				E_B_motor(300);
				E_L_motor(280);
				}else{
				E_B_motor(300);
				}
			}
			n=1;
			rflag = 0;
			lflag = 0;
 		 }
	}


}
//
int Left_Light()
{
	int color,n;
	n = SensorValue(L1);
	if(n > 68)
	{
		displayBigTextLine(1,"L1=%d,silver",n);
		color = SELBER;
	}else if(n > 50)
	{
		displayBigTextLine(1,"L1=%d,white",n);
		color = WHITE;
	}else
	{
		displayBigTextLine(1,"L1=%d,black",n);
		color = BLACK;
	}
	return color;
}
int Senter_Light()
{
	int color,n;
	n = SensorValue(L2);
	if(n > 45)
	{
		displayBigTextLine(3,"L2=%d,silver",n);
		color = SELBER;
	}else if(n > 10)
	{
		displayBigTextLine(3,"L2=%d,white",n);
		color = WHITE;
	}else
	{
		displayBigTextLine(3,"L2=%d,black",n);
		color = BLACK;
	}
	return color;
}
int Rigth_Light()
{
	int color,n;
	n = SensorValue(L3);
	if(n > 65)
	{
		displayBigTextLine(5,"L3=%d,silver",n);
		color = SELBER;
	}else if(n > 40)
	{
		displayBigTextLine(5,"L3=%d,white",n);
		color = WHITE;
	}else
	{
		displayBigTextLine(5,"L3=%d ,black",n);
		color = BLACK;
	}
	return color;
}
void Advance_motor()
{
	motor[motorA] = -20;
	motor[motorD] = -20;
}
void Rigth_motor()
{
	motor[motorA] = -20;
	motor[motorD] = 0;
}
void Left_motor()
{
	motor[motorA] = 0;
	motor[motorD] = -20;
}
void Back_motor()
{
	motor[motorA] = -20;
	motor[motorD] = -20;
}
void Stop_motor()
{
	motor[motorA] = 0;
	motor[motorD] = 0;
}
void E_A_motor(int n)
{
	nMotorEncoder[motorA] = 0;
	nMotorEncoder[motorD] = 0;
	while((nMotorEncoder[motorA] < n)||(nMotorEncoder[motorD] < n))
	{
		motor[motorA] = 20;
		motor[motorD] = 20;
	}
}
void E_R_motor(int n)
{
	nMotorEncoder[motorA] = 0;
	nMotorEncoder[motorD] = 0;
	while((nMotorEncoder[motorA] < n)||(nMotorEncoder[motorD] > -n))
	{
		motor[motorA] = 20;
		motor[motorD] = -20;
	}
}
void E_L_motor(int n)
{
	nMotorEncoder[motorA] = 0;
	nMotorEncoder[motorD] = 0;
	while((nMotorEncoder[motorA] > -n)||(nMotorEncoder[motorD] < n))
	{
		motor[motorA] = -20;
		motor[motorD] = 20;
	}
}
void E_B_motor(int n)
{
	nMotorEncoder[motorA] = 0;
	nMotorEncoder[motorD] = 0;
	while((nMotorEncoder[motorA] > -n)||(nMotorEncoder[motorD] > -n))
	{
		motor[motorA] = -20;
		motor[motorD] = -20;
	}
}
