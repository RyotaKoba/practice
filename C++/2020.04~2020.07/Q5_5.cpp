#include<stdio.h>

int main(void)
{
	int score[5][3];
	float sumA, sumB, sumC, sumD, sumE,sumMath,sumEng,sumJapnese;

	printf("���kA�̐��w�̓_���́H�F");
	scanf("%d", &score[0][0]);
	printf("���kA�̉p��̓_���́H�F");
	scanf("%d", &score[0][1]);
	printf("���kA�̍���̓_���́H�F");
	scanf("%d", &score[0][2]);
	printf("���kB�̐��w�̓_���́H�F");
	scanf("%d", &score[1][0]);
	printf("���kB�̉p��̓_���́H�F");
	scanf("%d", &score[1][1]);
	printf("���kB�̍���̓_���́H�F");
	scanf("%d", &score[1][2]);
	printf("���kC�̐��w�̓_���́H�F");
	scanf("%d", &score[2][0]);
	printf("���kC�̉p��̓_���́H�F");
	scanf("%d", &score[2][1]);
	printf("���kC�̍���̓_���́H�F");
	scanf("%d", &score[2][2]);
	printf("���kD�̐��w�̓_���́H�F");
	scanf("%d", &score[3][0]);
	printf("���kD�̉p��̓_���́H�F");
	scanf("%d", &score[3][1]);
	printf("���kD�̍���̓_���́H�F");
	scanf("%d", &score[3][2]);
	printf("���kE�̐��w�̓_���́H�F");
	scanf("%d", &score[4][0]);
	printf("���kE�̉p��̓_���́H�F");
	scanf("%d", &score[4][1]);
	printf("���kE�̍���̓_���́H�F");
	scanf("%d", &score[4][2]);
	sumA = (score[0][0] + score[0][1] + score[0][2]);
	sumB = (score[1][0] + score[1][1] + score[1][2]);
	sumC = (score[2][0] + score[2][1] + score[2][2]);
	sumD = (score[3][0] + score[3][1] + score[3][2]);
	sumE = (score[4][0] + score[4][1] + score[4][2]);
	sumMath = score[0][0] + score[1][0] + score[2][0] + score[3][0] + score[4][0];
	sumEng = score[0][1] + score[1][1] + score[2][1] + score[3][1] + score[4][1];
	sumJapnese = score[0][2] + score[1][2] + score[2][2] + score[3][2] + score[4][2];
	printf("\n");
	printf("�@�@�@���w�@�p��@����@����\n");
	printf("���kA  %2d    %2d    %2d   %.1f\n", score[0][0], score[0][1], score[0][2], sumA / 3.0);
	printf("���kB  %2d    %2d    %2d   %.1f\n", score[1][0], score[1][1], score[1][2], sumB / 3.0);
	printf("���kC  %2d    %2d    %2d   %.1f\n", score[2][0], score[2][1], score[2][2], sumC / 3.0);
	printf("���kD  %2d    %2d    %2d   %.1f\n", score[3][0], score[3][1], score[3][2], sumD / 3.0);
	printf("���kE  %2d    %2d    %2d   %.1f\n", score[4][0], score[4][1], score[4][2], sumE / 3.0);
	printf(" ���� %.1f  %.1f  %.1f  %.1f\n", sumMath / 5.0, sumEng / 5.0, sumJapnese / 5.0, ((sumA / 3.0) + (sumB / 3.0) + (sumC / 3.0) + (sumD / 3.0) + (sumE / 3.0)) / 5.0);
	return 0;
}