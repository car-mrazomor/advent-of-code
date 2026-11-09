#include <stdio.h>
#include <string.h>

int main(void) {
    char row[256];
    long ways[256] = {0}, next[256];
    int splits = 0, width = 0;
    while (scanf("%255s", row) == 1) {
        width = (int)strlen(row);
        memset(next, 0, sizeof next);
        for (int x = 0; x < width; x++) {
            if (row[x] == 'S') next[x] = 1;
            else if (row[x] == '^' && ways[x]) {
                splits++;
                if (x > 0) next[x - 1] += ways[x];
                if (x + 1 < width) next[x + 1] += ways[x];
            } else next[x] += ways[x];
        }
        memcpy(ways, next, sizeof ways);
    }
    long timelines = 0;
    for (int x = 0; x < width; x++) timelines += ways[x];
    printf("%d\n%ld\n", splits, timelines);
    return 0;
}
