#include<stdio.h>
#include<string.h>

int main(void)
{
	struct ningen
	{
		char shimei[11];
		int birth;
		float height;
	}student;

	strcpy(student.shimei, "���� ����");
	student.birth = 2001;
	student.height = 173.0;
	printf("�����F%s ���N�F%d �g���F%.1f(cm)\n", student.shimei, student.birth, student.height);
	return 0;
}