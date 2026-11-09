#include <stdio.h>

int main(void) {
    unsigned long secret, total = 0;
    while (scanf("%lu", &secret) == 1) {
        for (int i = 0; i < 2000; i++) {
            secret = (secret ^ (secret << 6)) & 0xFFFFFF;
            secret = (secret ^ (secret >> 5)) & 0xFFFFFF;
            secret = (secret ^ (secret << 11)) & 0xFFFFFF;
        }
        total += secret;
    }
    printf("%lu\n", total);
    return 0;
}
