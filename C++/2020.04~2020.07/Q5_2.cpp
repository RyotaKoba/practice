#include<stdio.h>

int main(void)
{
	float height[100] = { 165,178,169,175,170 };
	float set = 1;
	float sum;
	int i = 5;/*初期設定された人数*/
	int k;

	while (i < 100)
	{
		printf("%d人目の身長(cm):", i + 1);
		scanf("%f", &set);
		if (!(set == 0))
		{
			height[i] = set;
			i++;
		}
		else 
		{
			break;
		}
	} 
	sum = 0.0;
	for (k = 0; k < i + 1; k++)
	{
		sum += height[k];
	}
	printf("平均身長　%.2f(cm)\n", sum / (i + 1));
	return 0;
}