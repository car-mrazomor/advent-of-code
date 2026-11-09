#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char line[256];
    int safe = 0;
    while (fgets(line, sizeof line, stdin)) {
        int levels[32], n = 0, used;
        char *p = line;
        while (sscanf(p, "%d%n", &levels[n], &used) == 1) n++, p += used;
        if (n < 2) continue;
        int dir = levels[1] > levels[0] ? 1 : -1, ok = 1;
        for (int i = 1; i < n && ok; i++) {
            int step = (levels[i] - levels[i - 1]) * dir;
            ok = step >= 1 && step <= 3;
        }
        safe += ok;
    }
    printf("%d\n", safe);
    return 0;
}
