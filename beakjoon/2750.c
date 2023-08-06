#include <stdio.h>
#include <stdlib.h>

int main(){
    int len;
    scanf("%d", &len);
    
    int *arr = (int*)malloc(sizeof(int) * len);

    for(int i = 0; i < len; i++){
        scanf("%d", &arr[i]);
        for(int j = 0; j < i; j++){
            if(arr[i] < arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    
    for(int i = 0; i < len; i++){
        printf("%d\n", arr[i]);
    }
    return 0;
}