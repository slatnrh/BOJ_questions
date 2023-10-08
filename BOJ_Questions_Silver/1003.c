#include <stdio.h>

void fibonacci(int N){
    if(N==0)
        printf("%d %d\n", 1, 0);
    else{   //N>0
        int fibo[N+1][2];
        fibo[0][0] = 1;
        fibo[0][1] = 0;
        fibo[1][0] = 0;
        fibo[1][1] = 1;
     
        for(int i=2; i<N+1; i++){
            fibo[i][0] = fibo[i-1][0] + fibo[i-2][0];
            fibo[i][1] = fibo[i-1][1] + fibo[i-2][1];
        }
        printf("%d %d\n", fibo[N][0], fibo[N][1]);
    }
}

int main(void){
    int T;
    scanf("%d", &T);
 
    for(int i=0; i<T; i++){
        int N;
        scanf("%d", &N);
 
        fibonacci(N);
    }
}