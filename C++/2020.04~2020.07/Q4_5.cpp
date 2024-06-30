#include<stdio.h>

float average(float sample1, float sample2, float sample3);

int main(void)
{
	float s1 = 0.0;
	float s2 = 0.0;
	float s3 = 0.0;
	printf("一人目の体重を入力してください：");
	scanf("%f", &s1);
	printf("二人目の体重を入力してください：");
	scanf("%f", &s2);
	printf("三人目の体重を入力してください：");
	scanf("%f", &s3);
	printf("三人の体重の平均は　%.1f です。", average(s1, s2, s3));
}

float average(float sample1, float sample2, float sample3)
{
	float ave,sum;
	sum = sample1 + sample2 + sample3;
	ave = sum / 3.0;
	return ave;
}