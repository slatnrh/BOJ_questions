#include <stdio.h>

int main(){
    int arr[3];
    for(int i = 0; i < 3; i++){
        scanf("%d", &arr[i]);
    }

    int temp = 0;
    int arr_size = sizeof(arr) / sizeof(int);
    for(int i = 0; i < arr_size; i++){
        for(int j = 0; j < arr_size - i - 1; j++){
            if(arr[j] < arr[j + 1]){
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    printf("%d \n", arr[1]);
    
    return 0;
}