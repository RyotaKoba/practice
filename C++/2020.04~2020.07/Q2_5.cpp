#include<stdio.h>

int main(void)
{
	int stamp52, stamp82, total, oshiharai, oturi;
	printf("52�~�؎�����������߂ł��傤���H�F");
		scanf("%d", &stamp52);
	printf("82�~�؎�����������߂ł��傤���H�F");
	scanf("%d", &stamp82);
	total = stamp52 * 52 + stamp82 * 82;
	printf("���v%d�~�ɂȂ�܂��B�����𓊓����Ă��������B�F",total);
		scanf("%d", &oshiharai);
		oturi = oshiharai - total;
		printf("%d�~���a���肢�����܂��B���ނ��%d�~�ł��B\n", oshiharai, oturi);
		printf("�܂��̂����p�����҂����Ă���܂��B");
		return 0;
}