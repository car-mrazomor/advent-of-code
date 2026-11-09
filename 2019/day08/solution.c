#include <stdio.h>

#define LAYER (25 * 6)

int main(void) {
    int c, i = 0, counts[3] = {0}, best_zeros = 1 << 30, best = 0;
    while ((c = getchar()) != EOF) {
        if (c < '0' || c > '9') continue;
        if (c <= '2') counts[c - '0']++;
        if (++i % LAYER == 0) {
            if (counts[0] < best_zeros) {
                best_zeros = counts[0];
                best = counts[1] * counts[2];
            }
            counts[0] = counts[1] = counts[2] = 0;
        }
    }
    printf("%d\n", best);
    return 0;
}
