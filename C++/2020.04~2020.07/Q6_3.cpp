#include<stdio.h>

int main(void)
{
	char mojiretu[5];
	char moji[3];

	printf("全角は2文字以内、半角は4文字以内で書いてください。：");
	scanf("%s", mojiretu);
	moji[0] = mojiretu[0];
	moji[1] = mojiretu[1];
	moji[2] = '\0';
	printf("%s\n", moji);
	return 0;
}