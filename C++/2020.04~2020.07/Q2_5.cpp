#include<stdio.h>

int main(void)
{
	int stamp52, stamp82, total, oshiharai, oturi;
	printf("52円切手を何枚お求めでしょうか？：");
		scanf("%d", &stamp52);
	printf("82円切手を何枚お求めでしょうか？：");
	scanf("%d", &stamp82);
	total = stamp52 * 52 + stamp82 * 82;
	printf("合計%d円になります。お金を投入してください。：",total);
		scanf("%d", &oshiharai);
		oturi = oshiharai - total;
		printf("%d円お預かりいたします。お釣りは%d円です。\n", oshiharai, oturi);
		printf("またのご利用をお待ちしております。");
		return 0;
}