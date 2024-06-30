#include<stdio.h>

int main(void)
{
	int bango;
	float sample1, sample2,kotae;

	printf("任意の実数を二つ入力してください：");
	scanf("%f %f", &sample1, &sample2);
	printf("演算法を1～4の番号で選んでください。\n");
	printf(" 1.足し算　2.引き算　3.掛け算　4.割り算");
	scanf("%d", &bango);
	switch (bango)
	{
	case 1:
		kotae = sample1 + sample2;
		printf("答えは　%f です。", kotae);
		break;
	case 2:
		kotae = sample1 - sample2;
		printf("答えは　%f です。", kotae);
		break;
	case 3:
		kotae = sample1 * sample2;
		printf("答えは　%f です。", kotae);
		break;
	case 4:
		kotae = sample1 / sample2;
		printf("答えは　%f です。", kotae);
		break;
	default:
		printf("指定された番号の中から選択してください。");
	}
	return 0;
}