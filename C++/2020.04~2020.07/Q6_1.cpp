#include<stdio.h>

int main(void)
{
	char sentence[21];
	int i;

	printf("�S�p10�����ȓ��̕��͂���͂��Ă��������F");
	scanf("%s", sentence);
	for (i = 0; sentence[i] != '\0'; i++)
	{
		printf("%c", sentence[i]);
	}
}