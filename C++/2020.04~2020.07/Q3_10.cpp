#include<stdio.h>

int main(void)
{
	float salary;
	float persent;/*賃上げ率(%)*/
	float increaserate;/*賃上げ率(実数)*/
	int count = 0;/*年数*/

	printf("初任給を入力してください：");
	scanf("%f", &salary);
	printf("賃上げ率(%)を入力してください：");
	scanf("%f", &persent);
	increaserate = 1 + (persent / 100.0);

	while (count <= 30)
	{
		count++;
		salary = salary * increaserate;
		printf("入社%d年目の月給は%d万円です。\n", count, (int)salary);
	}
	return 0;
}