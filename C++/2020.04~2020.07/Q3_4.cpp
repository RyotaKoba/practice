#include<stdio.h>

int main(void)
{
	float height, weight, standard;

	printf("あなたの身長を入力してください：");
	scanf("%f", &height);
	printf("次にあなたの体重を入力してください：");
	scanf("%f", &weight);
	standard = (height / 100) * (height / 100) * 22;

	if (weight == 0 || height == 0)
	{
		printf("適切な数字を入力してください");
		return 0;
	}

	if (weight >= standard * 1.30)
	{
		printf("太りすぎ");
	}
	else if (weight >= standard * 1.15)
	{
		printf("太り気味");
	}
	else if (weight <= standard * 0.70)
	{
		printf("痩せすぎ");
	}
	else if (weight <= standard * 0.85)
	{
		printf("痩せ気味");
	}
	else
	{
		printf("普通");
	}
}