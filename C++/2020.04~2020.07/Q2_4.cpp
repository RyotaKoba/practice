#include<stdio.h>

int main(void)
{
	int warareru, waru, kotae, amari;

	printf("�D���Ȑ�������͂��Ă��������@�����鐔�F");
		scanf("%d", &warareru);
	printf("�D���Ȑ�������͂��Ă��������@���鐔�F");
		scanf("%d", &waru);
	kotae = warareru / waru;
	amari = warareru % waru;
	printf("�v�Z�̌��ʂ́@����%d �]�肪%d�@�ł�\n", kotae, amari);
	return 0;
}