#include <stdio.h>

int main() {
    int ans[8];
    int ascending = 1;
    int descending = 1;

    for (int i = 0; i < 8; i++) {
        scanf("%d", &ans[i]);
    }

    for (int i = 0; i < 7; i++) {
        if (ans[i] < ans[i + 1]) {
            descending = 0;
        } else if (ans[i] > ans[i + 1]) {
            ascending = 0;
        }
    }

    if (ascending) {
        printf("ascending");
    } else if (descending) {
        printf("descending");
    } else {
        printf("mixed");
    }

    return 0;
}