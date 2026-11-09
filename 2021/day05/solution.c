#include <stdio.h>

static unsigned char grid[1000][1000];

int main(void) {
    int x1, y1, x2, y2, overlaps = 0;
    while (scanf("%d,%d -> %d,%d", &x1, &y1, &x2, &y2) == 4) {
        if (x1 != x2 && y1 != y2) continue;
        int dx = (x2 > x1) - (x2 < x1), dy = (y2 > y1) - (y2 < y1);
        for (int x = x1, y = y1;; x += dx, y += dy) {
            if (++grid[y][x] == 2) overlaps++;
            if (x == x2 && y == y2) break;
        }
    }
    printf("%d\n", overlaps);
    return 0;
}
