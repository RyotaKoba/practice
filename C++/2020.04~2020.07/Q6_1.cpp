#include<stdio.h>

int main(void)
{
	char sentence[21];
	int i;

	printf("全角10文字以内の文章を入力してください：");
	scanf("%s", sentence);
	for (i = 0; sentence[i] != '\0'; i++)
	{
		printf("%c", sentence[i]);
	}
}