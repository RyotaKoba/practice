#include<stdio.h>

int main(void)
{
	float height, weight, standard;

	printf("���Ȃ��̐g������͂��Ă��������F");
	scanf("%f", &height);
	printf("���ɂ��Ȃ��̑̏d����͂��Ă��������F");
	scanf("%f", &weight);
	standard = (height / 100) * (height / 100) * 22;

	if (weight == 0 || height == 0)
	{
		printf("�K�؂Ȑ�������͂��Ă�������");
		return 0;
	}

	if (weight >= standard * 1.30)
	{
		printf("���肷��");
	}
	else if (weight >= standard * 1.15)
	{
		printf("����C��");
	}
	else if (weight <= standard * 0.70)
	{
		printf("��������");
	}
	else if (weight <= standard * 0.85)
	{
		printf("�����C��");
	}
	else
	{
		printf("����");
	}
}