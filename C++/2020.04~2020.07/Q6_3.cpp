#include<stdio.h>

int main(void)
{
	char mojiretu[5];
	char moji[3];

	printf("�S�p��2�����ȓ��A���p��4�����ȓ��ŏ����Ă��������B�F");
	scanf("%s", mojiretu);
	moji[0] = mojiretu[0];
	moji[1] = mojiretu[1];
	moji[2] = '\0';
	printf("%s\n", moji);
	return 0;
}