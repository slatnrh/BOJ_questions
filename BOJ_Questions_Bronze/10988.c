#include <stdio.h>
#include <string.h>

int main(){
    char arr[255];
    scanf("%s", arr);
    
    /* 배열 크기 구하기 */
    int size = 0;
    while(arr[size] != 0){
        size++;
    }
    size -= 1;
    
    int cnt = 0;
    while(cnt <= size){
        if(arr[cnt] != arr[size]){
            printf("0");
            return 0;
        }
        cnt++;
        size--;
    }
    
    printf("1");
    
    return 0;
}