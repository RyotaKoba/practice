#include<stdio.h>

float average(float sample1, float sample2, float sample3);

int main(void)
{
	float s1 = 0.0;
	float s2 = 0.0;
	float s3 = 0.0;
	printf("��l�ڂ̑̏d����͂��Ă��������F");
	scanf("%f", &s1);
	printf("��l�ڂ̑̏d����͂��Ă��������F");
	scanf("%f", &s2);
	printf("�O�l�ڂ̑̏d����͂��Ă��������F");
	scanf("%f", &s3);
	printf("�O�l�̑̏d�̕��ς́@%.1f �ł��B", average(s1, s2, s3));
}

float average(float sample1, float sample2, float sample3)
{
	float ave,sum;
	sum = sample1 + sample2 + sample3;
	ave = sum / 3.0;
	return ave;
}