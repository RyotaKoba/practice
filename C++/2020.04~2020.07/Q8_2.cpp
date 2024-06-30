#include<stdio.h>
#include<string.h>

typedef struct ningen
{
	char shimei[11];
	int birth;
	float height;
}HITO;

HITO list[5] = { {"小林 亮太",2001,173.0},{"田中 太郎",2000,175.3},{"朝雲 昭",2002,168.2},{"天馬 飛雄",1998,178.4},{"山田 花子",1997,165.9} };

int main(void)
{
	int i;

	printf("       　名前　　生年　　 身長\n");
	for (i = 0; i < 5; i++)
	{
		printf("%15s %4d年   %.1f\n", list[i].shimei, list[i].birth, list[i].height);
	}
	return 0;
}