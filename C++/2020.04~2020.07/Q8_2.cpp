#include<stdio.h>
#include<string.h>

typedef struct ningen
{
	char shimei[11];
	int birth;
	float height;
}HITO;

HITO list[5] = { {"���� ����",2001,173.0},{"�c�� ���Y",2000,175.3},{"���_ ��",2002,168.2},{"�V�n ��Y",1998,178.4},{"�R�c �Ԏq",1997,165.9} };

int main(void)
{
	int i;

	printf("       �@���O�@�@���N�@�@ �g��\n");
	for (i = 0; i < 5; i++)
	{
		printf("%15s %4d�N   %.1f\n", list[i].shimei, list[i].birth, list[i].height);
	}
	return 0;
}