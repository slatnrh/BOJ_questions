#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);

    while (T--) {
        int N, M;
        scanf("%d %d", &N, &M);

        int i = 0;

        while (1) {
            if (N % 2 == 0 && 2 * M >= N) {
                i += N / 2;
                printf("%d\n", i);
                break;
            }
            if (N % 2 == 0 && 2 * M < N) {
                i += M;
                if (N - M < 0) {
                    break;
                }
                N -= M;
            }
            if (N % 2 == 1 && N < 3 * M) {
                i += M + (N - M) / 2;
                printf("%d\n", i);
                break;
            }
            if (N % 2 == 1 && N >= 3 * M) {
                N -= M;
                i += M;
            }
        }
    }

    return 0;
}