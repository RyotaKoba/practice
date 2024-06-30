#include<stdio.h>

int main(void)
{
	float calorie; /*摂取カロリー*/
	float sum = 0.0;/*摂取カロリーの合計*/

	printf("朝食での摂取カロリー(cal)を入力してください：");
	scanf("%f", &calorie);
	sum += calorie;
	printf("昼食での摂取カロリー(cal)を入力してください：");
	scanf("%f", &calorie);
	sum += calorie;
	printf("夕食での摂取カロリー(cal)を入力してください：");
	scanf("%f", &calorie);
	sum += calorie;
	printf("本日の合計摂取カロリーは %.2f (cal)です。\n", sum);
	return 0;
}