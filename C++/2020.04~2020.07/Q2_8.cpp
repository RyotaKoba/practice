#include<stdio.h>

int main(void)
{
	float calorie; /*�ێ�J�����[*/
	float sum = 0.0;/*�ێ�J�����[�̍��v*/

	printf("���H�ł̐ێ�J�����[(cal)����͂��Ă��������F");
	scanf("%f", &calorie);
	sum += calorie;
	printf("���H�ł̐ێ�J�����[(cal)����͂��Ă��������F");
	scanf("%f", &calorie);
	sum += calorie;
	printf("�[�H�ł̐ێ�J�����[(cal)����͂��Ă��������F");
	scanf("%f", &calorie);
	sum += calorie;
	printf("�{���̍��v�ێ�J�����[�� %.2f (cal)�ł��B\n", sum);
	return 0;
}