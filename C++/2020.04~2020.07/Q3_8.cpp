#include<stdio.h>

/*���C��19���Ŗ��N3.5�����グ������ЂɁA22�΂ŏA�E����B
�@������50�����z����͉̂��΂ɂȂ邩���ׂ�*/
int main(void)
{
	float salary = 19.0;/*���C��*/
	int age = 22;/*���Ў��̔N��*/
	int count = 0;/*�N��*/

	while (salary < 50.0)
	{
		age++;
		count++;
		salary = salary * 1.035;
	}
	printf("���Ђ���%d�N�A%d�΂ɂ��Č���50�����z�������I",count,age);
	return 0;
}