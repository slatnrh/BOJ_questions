#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    srand((int)time(NULL));
    for(int i = 0; i < 5; i++){
        printf("정수 출력: %d\n", rand());
    }

    return 0;
}