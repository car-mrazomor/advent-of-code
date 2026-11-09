#include <stdio.h>

int main(void) {
    char s[8192];
    scanf("%8191s", s);
    for (int i = 4; s[i - 1]; i++) {
        unsigned seen = 0;
        int distinct = 1;
        for (int j = i - 4; j < i; j++) {
            if (seen >> (s[j] - 'a') & 1) distinct = 0;
            seen |= 1u << (s[j] - 'a');
        }
        if (distinct) {
            printf("%d\n", i);
            return 0;
        }
    }
    return 1;
}
