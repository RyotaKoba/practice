#include<stdio.h>

int main(void)
{
	int zekomi;
	float hontai,shohi;

	printf("�ō��݉��i����͂��Ă��������F");
	scanf("%d", &zekomi);
	hontai = (float)zekomi / 1.08;
	shohi = (float)zekomi - hontai;
	printf("�ō����i %d �~\n�{�̉��i %d �~\n����Ŋz�@%d �~", zekomi, (int)hontai, (int)shohi);
	return 0;
}