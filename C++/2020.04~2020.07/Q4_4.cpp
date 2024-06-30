#include<stdio.h>

int agecheck(int a);

int main(void)
{
	int age,check;
	printf("年齢を入力してください：");
	scanf("%d", &age);
	check = agecheck(age);
	if (check == 3)
	{
		printf("シニア");
	}
	else if (check == 2)
	{
		printf("成年");
	}
	else if (check == 1)
	{
		printf("未成人");
	}
	else if (check == 0)
	{
		printf("入力エラー");
	}
}

int agecheck(int a)
{
	int b;

	if (a >= 65)
	{
		b = 3;
	}
	else if (a >= 20 && 64 <= a)
	{
		b = 2;
	}
	else if (a >= 0 && 19 <= a)
	{
		b = 1;
	}
	else if (a < 0)
	{
		b = 0;
	}
	return b;
}