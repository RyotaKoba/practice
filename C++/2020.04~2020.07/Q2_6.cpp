#include<stdio.h>

int main(void)
{
	int zekomi;
	float hontai,shohi;

	printf("税込み価格を入力してください：");
	scanf("%d", &zekomi);
	hontai = (float)zekomi / 1.08;
	shohi = (float)zekomi - hontai;
	printf("税込価格 %d 円\n本体価格 %d 円\n消費税額　%d 円", zekomi, (int)hontai, (int)shohi);
	return 0;
}