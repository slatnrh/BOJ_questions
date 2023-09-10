#include <stdio.h>

int main() {
	int N;
	int mul5 = 0;	// 5의 배수
	int mul25 = 0;	// 25의 배수
	int mul125 = 0;	// 125의 배수

	scanf("%d", &N);

	mul5 = N / 5;
	mul25 = N / 25;
	mul125 = N / 125;

	printf("%d\n", mul5 + mul25 + mul125);

	return 0;
}