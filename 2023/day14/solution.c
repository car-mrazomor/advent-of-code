#include <stdio.h>
#include <string.h>

static char map[128][128];

int main(void) {
    int rows = 0;
    while (scanf("%127s", map[rows]) == 1) rows++;
    int cols = (int)strlen(map[0]);
    long load = 0;
    for (int x = 0; x < cols; x++) {
        int free = 0;
        for (int y = 0; y < rows; y++) {
            if (map[y][x] == '#') free = y + 1;
            else if (map[y][x] == 'O') load += rows - free++;
        }
    }
    printf("%ld\n", load);
    return 0;
}
