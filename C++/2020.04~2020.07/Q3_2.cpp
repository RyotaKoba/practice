#include<stdio.h>

int main(void)
{
	int age;

	printf("年齢を入力してください：");
	scanf("%d", &age);
	if ((age < 3) || (age >= 70))
	{
		printf("入場無料");
	}
	return 0;
}