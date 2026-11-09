#include <stdio.h>
#include <string.h>

int main(void) {
    char line[64];
    unsigned any = 0, all = ~0u;
    int sum_any = 0, sum_all = 0, people = 0;
    for (;;) {
        char *got = fgets(line, sizeof line, stdin);
        if (!got || line[0] == '\n') {
            if (people) {
                sum_any += __builtin_popcount(any);
                sum_all += __builtin_popcount(all);
            }
            any = 0, all = ~0u, people = 0;
            if (!got) break;
            continue;
        }
        unsigned mine = 0;
        for (char *c = line; *c >= 'a' && *c <= 'z'; c++) mine |= 1u << (*c - 'a');
        any |= mine, all &= mine, people++;
    }
    printf("%d\n%d\n", sum_any, sum_all);
    return 0;
}
