#include<stdio.h>

int main(void)
{
	int wakeup;

	do
	{
		printf("�u���[���A�N����`�v\n");
		printf("1.�N����@2.�܂������@3.�n����\n");
		scanf("%d", &wakeup);
		if (wakeup == 1)
		{
			printf("�u���͂悤�`�v\n");
		}
		else if (wakeup == 2)
		{
			printf("�u�܂������`�v\n");
		}
		else if (wakeup == 3)
		{
			printf("�uZZZZZ�v\n");
		}
		else
		{
			printf("�u�E�E�E�E�E�v\n");
		}
	} while (!(wakeup == 1));
}