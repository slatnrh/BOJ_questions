#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);
    
    /* 위에 n-1개의 줄 */
    for(int i = 1; i < num; i++){
        for(int j = num - i; j >= 1; j--){
            printf(" ");
        }
        for(int k = 0; k < 2*i - 1; k++){
            printf("*");
        }
        printf("\n");
    }
    
    /* 밑에 n개의 줄 */
    for(int i = num; i >= 1; i--){
        for(int j = num - i; j >= 1; j--){
            printf(" ");
        }
        for(int k = 0; k < 2*i - 1; k++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}