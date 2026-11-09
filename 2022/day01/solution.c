#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char line[64];
    long current = 0, top[3] = {0};
    for (;;) {
        char *got = fgets(line, sizeof line, stdin);
        if (!got || line[0] == '\n') {
            for (int i = 0; i < 3; i++)
                if (current > top[i]) {
                    long swap = top[i];
                    top[i] = current;
                    current = swap;
                }
            current = 0;
            if (!got) break;
        } else {
            current += atol(line);
        }
    }
    printf("%ld\n%ld\n", top[0], top[0] + top[1] + top[2]);
    return 0;
}
