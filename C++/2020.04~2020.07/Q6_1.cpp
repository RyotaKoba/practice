#include<stdio.h>

int main(void)
{
	char sentence[21];
	int i;

	printf("‘SŠp10•¶šˆÈ“à‚Ì•¶Í‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢F");
	scanf("%s", sentence);
	for (i = 0; sentence[i] != '\0'; i++)
	{
		printf("%c", sentence[i]);
	}
}