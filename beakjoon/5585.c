#include <stdio.h>

int main(){
    int money;
    scanf("%d", &money);
    money = 1000 - money;
    
    int cnt = 0;
    while(1){
        if(money == 0){
            break;
        }
        
        if(money >= 500){
            money -= 500;
            cnt++;
        }
        else if(money >= 100){
            money -= 100;
            cnt++;
        }
        else if(money >= 50){
            money -= 50;
            cnt++;
        }
        else if(money >= 10){
            money -= 10;
            cnt++;
        }
        else if(money >= 5){
            money -= 5;
            cnt++;
        }
        else if(money >= 1){
            money -= 1;
            cnt++;
        }
    }
    
    printf("%d", cnt);
    
    return 0;
}