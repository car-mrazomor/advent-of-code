#include <stdio.h>
#include <string.h>

static int priority(char c) { return c >= 'a' ? c - 'a' + 1 : c - 'A' + 27; }

int main(void) {
    char sack[128];
    int sum = 0;
    while (scanf("%127s", sack) == 1) {
        int half = (int)strlen(sack) / 2;
        unsigned long long first = 0;
        for (int i = 0; i < half; i++) first |= 1ULL << priority(sack[i]);
        for (int i = half; sack[i]; i++)
            if (first >> priority(sack[i]) & 1) {
                sum += priority(sack[i]);
                break;
            }
    }
    printf("%d\n", sum);
    return 0;
}
