#include <stdio.h>

int main() {
    int num1, num2, num3, num4, num5;
    scanf("%d %d %d %d %d", &num1, &num2, &num3, &num4, &num5);
    
    int ans = (num1*num1) + (num2*num2) + (num3*num3) + (num4*num4) + (num5*num5);
    printf("%d", ans%10);

    return 0;
}