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

	strcpy(student.shimei, "小林 亮太");
	student.birth = 2001;
	student.height = 173.0;
	printf("氏名：%s 生年：%d 身長：%.1f(cm)\n", student.shimei, student.birth, student.height);
	return 0;
}