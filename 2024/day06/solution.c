#include <stdio.h>
#include <string.h>

static char map[160][160];

int main(void) {
    int rows = 0, y = 0, x = 0;
    while (scanf("%159s", map[rows]) == 1) {
        char *g = strchr(map[rows], '^');
        if (g) y = rows, x = (int)(g - map[rows]);
        rows++;
    }
    int cols = (int)strlen(map[0]), dy = -1, dx = 0, visited = 0;
    for (;;) {
        if (map[y][x] != 'X') map[y][x] = 'X', visited++;
        int ny = y + dy, nx = x + dx;
        if (ny < 0 || ny >= rows || nx < 0 || nx >= cols) break;
        if (map[ny][nx] == '#') {
            int t = dy;
            dy = dx, dx = -t;
        } else {
            y = ny, x = nx;
        }
    }
    printf("%d\n", visited);
    return 0;
}
