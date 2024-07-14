#pragma config(Sensor, S1,     L1,             sensorLightActive)
#pragma config(Sensor, S2,     L2,             sensorEV3_Color)
#pragma config(Sensor, S3,     L3,             sensorLightActive)
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
//L
int Ldata = 0;
void L_motor_encoder(int p);
//main

task main()
{
	int flag = 0;
	int r,s,l;
	nMotorEncoder[motorA]= 0;
	nMotorEncoder[motorB]= 0;
	nMotorEncoder[motorC]= 0;
	while(true)
	{
		L_motor_encoder(180);
		L_motor_encoder(-180);
		Advance_motor();
	}

}

//
int Left_Light()
{
	int color,n;
	n = SensorValue(L1);
	if(n > 52)
	{
		displayBigTextLine(1,"L1=%d,silver",n);
		color = SELBER;
	}else if(n > 32)
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
	if(n > 30)
	{
		displayBigTextLine(3,"L2=%d,silver",n);
		color = SELBER;
	}else if(n > 5)
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
	if(n > 52)
	{
		displayBigTextLine(5,"L3=%d,silver",n);
		color = SELBER;
	}else if(n > 32)
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
	motor[motorA] = -32;
	motor[motorD] = -32;
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
	motor[motorA] = 20;
	motor[motorD] = 20;
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
		motor[motorA] = 30;
		motor[motorD] = 30;
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
void L_motor_encoder(int p)
{
	int np,d;
	np=nMotorEncoder[motorB];
	d = p-np;
	if(d>0)
	{
		motor[motorB] = 0;
		while(nMotorEncoder[motorB]<p){}
		motor[motorB] = 90;
		while(nMotorEncoder[motorB]>p){}
		motor[motorB] = 0;
		}else{
		motor[motorB] = -40;
		while(nMotorEncoder[motorB]>p){}
		motor[motorB]= 10;
		while(nMotorEncoder[motorB]<p){}
		motor[motorB]= 0;
	}
}
