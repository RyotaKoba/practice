#include<stdio.h>

int main(void)
{
	int wakeup;

	do
	{
		printf("「おーい、起きろ～」\n");
		printf("1.起きる　2.まだ眠い　3.熟睡中\n");
		scanf("%d", &wakeup);
		if (wakeup == 1)
		{
			printf("「おはよう～」\n");
		}
		else if (wakeup == 2)
		{
			printf("「まだ眠い～」\n");
		}
		else if (wakeup == 3)
		{
			printf("「ZZZZZ」\n");
		}
		else
		{
			printf("「・・・・・」\n");
		}
	} while (!(wakeup == 1));
}