#include<stdio.h>

int main(void)
{
	int kazu;

	printf("好きな整数を入力してください：");
		scanf("%d", &kazu);
	printf("あなたの好きな数は %d ですね。\n", kazu);
	return 0;
}