#include<stdio.h>

int main(void)
{
	char mojiretu[100];
	int i,c;

	printf("�C�ӂ̃A���t�@�x�b�g�̕��������͂��Ă��������F");
	scanf("%s", mojiretu);

	for (i = 0; mojiretu[i] != '\0'; i++)
	{
		if ('a' <= mojiretu[i] && mojiretu[i] <= 'z')
		{
			mojiretu[i] -= 32;
			printf("%c", mojiretu[i]);
		}
		else {
			printf("%c", mojiretu[i]);
		}
	}
	return 0;
}