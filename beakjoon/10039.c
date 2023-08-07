#include <stdio.h>

int main() {
    int score;
    int rslt = 0;
    for(int i = 0; i < 5; i++){
        scanf("%d", &score);
        if(score < 40){
            score = 40;
        }
        rslt += score;
    }
    printf("%d", rslt / 5);
    
    return 0;
}