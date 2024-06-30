#include<stdio.h>

/*初任給19万で毎年3.5％賃上げされる会社に、22歳で就職する。
　月給が50万を越えるのは何歳になるか調べる*/
int main(void)
{
	float salary = 19.0;/*初任給*/
	int age = 22;/*入社時の年齢*/
	int count = 0;/*年数*/

	while (salary < 50.0)
	{
		age++;
		count++;
		salary = salary * 1.035;
	}
	printf("入社から%d年、%d歳にして月給50万を越えたぞ！",count,age);
	return 0;
}