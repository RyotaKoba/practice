#include<stdio.h>

int main(void)
{
	int bango;
	float sample1, sample2,kotae;

	printf("�C�ӂ̎��������͂��Ă��������F");
	scanf("%f %f", &sample1, &sample2);
	printf("���Z�@��1�`4�̔ԍ��őI��ł��������B\n");
	printf(" 1.�����Z�@2.�����Z�@3.�|���Z�@4.����Z");
	scanf("%d", &bango);
	switch (bango)
	{
	case 1:
		kotae = sample1 + sample2;
		printf("�����́@%f �ł��B", kotae);
		break;
	case 2:
		kotae = sample1 - sample2;
		printf("�����́@%f �ł��B", kotae);
		break;
	case 3:
		kotae = sample1 * sample2;
		printf("�����́@%f �ł��B", kotae);
		break;
	case 4:
		kotae = sample1 / sample2;
		printf("�����́@%f �ł��B", kotae);
		break;
	default:
		printf("�w�肳�ꂽ�ԍ��̒�����I�����Ă��������B");
	}
	return 0;
}