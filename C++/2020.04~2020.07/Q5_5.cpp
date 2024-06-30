#include<stdio.h>

int main(void)
{
	int score[5][3];
	float sumA, sumB, sumC, sumD, sumE,sumMath,sumEng,sumJapnese;

	printf("生徒Aの数学の点数は？：");
	scanf("%d", &score[0][0]);
	printf("生徒Aの英語の点数は？：");
	scanf("%d", &score[0][1]);
	printf("生徒Aの国語の点数は？：");
	scanf("%d", &score[0][2]);
	printf("生徒Bの数学の点数は？：");
	scanf("%d", &score[1][0]);
	printf("生徒Bの英語の点数は？：");
	scanf("%d", &score[1][1]);
	printf("生徒Bの国語の点数は？：");
	scanf("%d", &score[1][2]);
	printf("生徒Cの数学の点数は？：");
	scanf("%d", &score[2][0]);
	printf("生徒Cの英語の点数は？：");
	scanf("%d", &score[2][1]);
	printf("生徒Cの国語の点数は？：");
	scanf("%d", &score[2][2]);
	printf("生徒Dの数学の点数は？：");
	scanf("%d", &score[3][0]);
	printf("生徒Dの英語の点数は？：");
	scanf("%d", &score[3][1]);
	printf("生徒Dの国語の点数は？：");
	scanf("%d", &score[3][2]);
	printf("生徒Eの数学の点数は？：");
	scanf("%d", &score[4][0]);
	printf("生徒Eの英語の点数は？：");
	scanf("%d", &score[4][1]);
	printf("生徒Eの国語の点数は？：");
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
	printf("　　　数学　英語　国語　平均\n");
	printf("生徒A  %2d    %2d    %2d   %.1f\n", score[0][0], score[0][1], score[0][2], sumA / 3.0);
	printf("生徒B  %2d    %2d    %2d   %.1f\n", score[1][0], score[1][1], score[1][2], sumB / 3.0);
	printf("生徒C  %2d    %2d    %2d   %.1f\n", score[2][0], score[2][1], score[2][2], sumC / 3.0);
	printf("生徒D  %2d    %2d    %2d   %.1f\n", score[3][0], score[3][1], score[3][2], sumD / 3.0);
	printf("生徒E  %2d    %2d    %2d   %.1f\n", score[4][0], score[4][1], score[4][2], sumE / 3.0);
	printf(" 平均 %.1f  %.1f  %.1f  %.1f\n", sumMath / 5.0, sumEng / 5.0, sumJapnese / 5.0, ((sumA / 3.0) + (sumB / 3.0) + (sumC / 3.0) + (sumD / 3.0) + (sumE / 3.0)) / 5.0);
	return 0;
}