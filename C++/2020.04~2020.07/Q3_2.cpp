#include<stdio.h>

int main(void)
{
	int age;

	printf("�N�����͂��Ă��������F");
	scanf("%d", &age);
	if ((age < 3) || (age >= 70))
	{
		printf("���ꖳ��");
	}
	return 0;
}