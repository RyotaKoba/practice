#include<stdio.h>

int main(void)
{
	float salary;
	float persent;/*���グ��(%)*/
	float increaserate;/*���グ��(����)*/
	int count = 0;/*�N��*/

	printf("���C������͂��Ă��������F");
	scanf("%f", &salary);
	printf("���グ��(%)����͂��Ă��������F");
	scanf("%f", &persent);
	increaserate = 1 + (persent / 100.0);

	while (count <= 30)
	{
		count++;
		salary = salary * increaserate;
		printf("����%d�N�ڂ̌�����%d���~�ł��B\n", count, (int)salary);
	}
	return 0;
}