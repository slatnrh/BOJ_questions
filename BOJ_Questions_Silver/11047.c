#include <stdio.h>
#include <stdlib.h>

int main() {
    int N, K;
    scanf("%d %d", &N, &K);
    
    int *arr = (int*)malloc(sizeof(int) * N);
    for(int i = 0; i < N; i++){
        scanf("%d", &arr[i]);
    }
    
    int rslt = 0;
    for(int i = N-1; i >= 0; i--){
        while(K >= arr[i]){
            K -= arr[i];
            rslt++;
        }
    }
    
    printf("%d", rslt);
    
    return 0;
}