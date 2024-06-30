#include<stdio.h>

int main(void)
{
	int zekomi;
	float hontai,shohi;

	printf("Å‚İ‰¿Ši‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢F");
	scanf("%d", &zekomi);
	hontai = (float)zekomi / 1.08;
	shohi = (float)zekomi - hontai;
	printf("Å‰¿Ši %d ‰~\n–{‘Ì‰¿Ši %d ‰~\nÁ”ïÅŠz@%d ‰~", zekomi, (int)hontai, (int)shohi);
	return 0;
}