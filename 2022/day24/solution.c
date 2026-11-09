#include <stdio.h>
#include <string.h>

#define MAX 160

static char map[MAX][MAX];
static unsigned char now[MAX][MAX], next[MAX][MAX];

static int mod(int a, int m) { return ((a % m) + m) % m; }

int main(void) {
    int rows = 0;
    while (scanf("%159s", map[rows]) == 1) rows++;
    int cols = (int)strlen(map[0]), h = rows - 2, w = cols - 2;
    now[0][1] = 1;
    for (int minute = 1;; minute++) {
        memset(next, 0, sizeof next);
        for (int y = 0; y < rows; y++)
            for (int x = 0; x < cols; x++) {
                if (!now[y][x]) continue;
                static const int dy[] = {0, 1, -1, 0, 0}, dx[] = {0, 0, 0, 1, -1};
                for (int d = 0; d < 5; d++) {
                    int ny = y + dy[d], nx = x + dx[d];
                    if (ny < 0 || ny >= rows || map[ny][nx] == '#') continue;
                    if (ny == rows - 1) {
                        printf("%d\n", minute);
                        return 0;
                    }
                    int iy = ny - 1, ix = nx - 1, blocked = 0;
                    if (ny > 0) {
                        blocked |= map[1 + iy][1 + mod(ix - minute, w)] == '>';
                        blocked |= map[1 + iy][1 + mod(ix + minute, w)] == '<';
                        blocked |= map[1 + mod(iy - minute, h)][1 + ix] == 'v';
                        blocked |= map[1 + mod(iy + minute, h)][1 + ix] == '^';
                    }
                    if (!blocked) next[ny][nx] = 1;
                }
            }
        memcpy(now, next, sizeof now);
    }
}
