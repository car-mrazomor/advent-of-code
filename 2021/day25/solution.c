#include <stdio.h>
#include <string.h>

static char map[160][160], next[160][160];

int main(void) {
    int rows = 0, cols = 0;
    while (scanf("%159s", map[rows]) == 1) rows++;
    cols = (int)strlen(map[0]);
    for (int step = 1;; step++) {
        int moved = 0;
        memcpy(next, map, sizeof map);
        for (int y = 0; y < rows; y++)
            for (int x = 0; x < cols; x++)
                if (map[y][x] == '>' && map[y][(x + 1) % cols] == '.') next[y][x] = '.', next[y][(x + 1) % cols] = '>', moved = 1;
        memcpy(map, next, sizeof map);
        for (int y = 0; y < rows; y++)
            for (int x = 0; x < cols; x++)
                if (map[y][x] == 'v' && map[(y + 1) % rows][x] == '.') next[y][x] = '.', next[(y + 1) % rows][x] = 'v', moved = 1;
        memcpy(map, next, sizeof map);
        if (!moved) {
            printf("%d\n", step);
            return 0;
        }
    }
}
