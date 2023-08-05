#include <stdio.h>

int main() {
    int k, n, m, cnt;
    scanf("%d", &k);
    
    for(int i = 0; i < k; i++){
        cnt = 1;
        scanf("%d %d", &n, &m);
        for(int z = 0; z < n; z++){
            cnt *= m - z;
            cnt /= 1 + z;
        }
        printf("%d\n", cnt);
    }
    

	return 0;
}