#include <stdio.h>

void GCD_AND_LCM(int num1, int num2){
    int gcd = 0, lcm = 0;
    for(int i = 1; i <= num1 && i <= num2; i++){
        if(num1 % i == 0 && num2 % i == 0){
            gcd = i;
        }
    }
    lcm = (num1 * num2) / gcd;
    printf("%d\n", gcd);
    printf("%d\n", lcm);
}

int main() {
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    
    GCD_AND_LCM(num1, num2);

    return 0;
}