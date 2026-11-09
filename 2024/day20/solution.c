#include <stdio.h>
#include <string.h>

#ifndef SAVE
#define SAVE 100
#endif

static char map[160][160];
static int dist[160][160];

int main(void) {
    int rows = 0, y = 0, x = 0;
    while (scanf("%159s", map[rows]) == 1) {
        char *s = strchr(map[rows], 'S');
        if (s) y = rows, x = (int)(s - map[rows]);
        rows++;
    }
    int cols = (int)strlen(map[0]);
    memset(dist, -1, sizeof dist);
    static const int dy[] = {1, -1, 0, 0}, dx[] = {0, 0, 1, -1};
    for (int step = 0;; step++) {
        dist[y][x] = step;
        if (map[y][x] == 'E') break;
        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d], nx = x + dx[d];
            if (map[ny][nx] != '#' && dist[ny][nx] < 0) {
                y = ny, x = nx;
                break;
            }
        }
    }
    int cheats = 0;
    for (int cy = 0; cy < rows; cy++)
        for (int cx = 0; cx < cols; cx++) {
            if (dist[cy][cx] < 0) continue;
            for (int d = 0; d < 4; d++) {
                int ny = cy + 2 * dy[d], nx = cx + 2 * dx[d];
                if (ny < 0 || ny >= rows || nx < 0 || nx >= cols || dist[ny][nx] < 0) continue;
                cheats += dist[ny][nx] - dist[cy][cx] - 2 >= SAVE;
            }
        }
    printf("%d\n", cheats);
    return 0;
}
