#include <stdio.h>
#include <stdlib.h>

int main() {
    int person_number;
    scanf("%d", &person_number);
    
    int *arr = (int*)malloc(sizeof(int) * person_number);
    
    for(int i = 0; i < person_number; i++){
        scanf("%d", &arr[i]);
        for(int j = 0; j < i; j++){
            if(arr[i] < arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    
    int rslt = 0;
    for(int i = 0; i < person_number; i++){
        for(int j = 0; j <= i; j++){
            rslt += arr[j];
        }
    }

    printf("%d", rslt);
    
    return 0;
}