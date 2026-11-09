#include <stdio.h>
#include <string.h>

#define MAX 200

static char map[MAX][MAX];
static int dist[MAX][MAX], queue[MAX * MAX][2];

int main(void) {
    int rows = 0, cols = 0, sy = 0, sx = 0, ey = 0, ex = 0;
    while (scanf("%199s", map[rows]) == 1) rows++;
    cols = (int)strlen(map[0]);
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++) {
            if (map[y][x] == 'S') sy = y, sx = x, map[y][x] = 'a';
            if (map[y][x] == 'E') ey = y, ex = x, map[y][x] = 'z';
            dist[y][x] = -1;
        }
    int head = 0, tail = 0;
    dist[sy][sx] = 0;
    queue[tail][0] = sy, queue[tail++][1] = sx;
    static const int dy[] = {1, -1, 0, 0}, dx[] = {0, 0, 1, -1};
    while (head < tail) {
        int y = queue[head][0], x = queue[head++][1];
        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d], nx = x + dx[d];
            if (ny < 0 || ny >= rows || nx < 0 || nx >= cols || dist[ny][nx] >= 0 || map[ny][nx] > map[y][x] + 1) continue;
            dist[ny][nx] = dist[y][x] + 1;
            queue[tail][0] = ny, queue[tail++][1] = nx;
        }
    }
    printf("%d\n", dist[ey][ex]);
    return 0;
}
