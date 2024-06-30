#include<stdio.h>

int main(void)
{
	int warareru, waru, kotae, amari;

	printf("好きな整数を入力してください　割られる数：");
		scanf("%d", &warareru);
	printf("好きな整数を入力してください　割る数：");
		scanf("%d", &waru);
	kotae = warareru / waru;
	amari = warareru % waru;
	printf("計算の結果は　商が%d 余りが%d　です\n", kotae, amari);
	return 0;
}