#include <stdio.h>
#include <string.h>

#ifndef STEPS
#define STEPS 64
#endif

static char map[160][160];
static int dist[160][160], queue[160 * 160][2];

int main(void) {
    int rows = 0;
    while (scanf("%159s", map[rows]) == 1) rows++;
    int cols = (int)strlen(map[0]), head = 0, tail = 0;
    memset(dist, -1, sizeof dist);
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++)
            if (map[y][x] == 'S') dist[y][x] = 0, queue[tail][0] = y, queue[tail++][1] = x;
    static const int dy[] = {1, -1, 0, 0}, dx[] = {0, 0, 1, -1};
    int reachable = 0;
    while (head < tail) {
        int y = queue[head][0], x = queue[head++][1];
        if (dist[y][x] % 2 == STEPS % 2) reachable++;
        if (dist[y][x] == STEPS) continue;
        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d], nx = x + dx[d];
            if (ny < 0 || ny >= rows || nx < 0 || nx >= cols || map[ny][nx] == '#' || dist[ny][nx] >= 0) continue;
            dist[ny][nx] = dist[y][x] + 1;
            queue[tail][0] = ny, queue[tail++][1] = nx;
        }
    }
    printf("%d\n", reachable);
    return 0;
}
