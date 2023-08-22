#include <stdio.h>
#include <stdlib.h>

int main(){
    printf("난수의 범위: 0부터 %d까지\n", RAND_MAX);
    for(int i = 0; i < 5; i++){
        printf("난수 출력: %d\n", rand());
    }

    return 0;
}