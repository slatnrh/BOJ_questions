#include <stdio.h>
#include <stdlib.h>

int main() {
    int seed;
    printf("씨드 값 입력: ");
    scanf("%d", &seed);
    srand(seed);
    
    for(int i = 0; i < 5; i++){
        printf("정수 출력: %d\n", rand());
    }
    
    return 0;
}