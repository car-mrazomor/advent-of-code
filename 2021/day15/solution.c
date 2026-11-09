#include <limits.h>
#include <stdio.h>
#include <string.h>

#define MAX 128
#define BUCKETS (MAX * MAX * 10)

static int risk[MAX][MAX], best[MAX][MAX];
static int queue_y[BUCKETS * 2], queue_x[BUCKETS * 2], head[BUCKETS], next_in[BUCKETS * 2], used;

static void push(int cost, int y, int x) {
    queue_y[used] = y, queue_x[used] = x, next_in[used] = head[cost], head[cost] = used++;
}

int main(void) {
    char line[MAX + 2];
    int rows = 0, cols = 0;
    while (scanf("%129s", line) == 1) {
        cols = (int)strlen(line);
        for (int x = 0; x < cols; x++) risk[rows][x] = line[x] - '0';
        rows++;
    }
    memset(head, -1, sizeof head);
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++) best[y][x] = INT_MAX;
    best[0][0] = 0;
    push(0, 0, 0);
    static const int dy[] = {1, -1, 0, 0}, dx[] = {0, 0, 1, -1};
    for (int cost = 0; cost < BUCKETS; cost++)
        for (int i = head[cost]; i != -1; i = next_in[i]) {
            int y = queue_y[i], x = queue_x[i];
            if (best[y][x] != cost) continue;
            if (y == rows - 1 && x == cols - 1) {
                printf("%d\n", cost);
                return 0;
            }
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d], nx = x + dx[d];
                if (ny < 0 || ny >= rows || nx < 0 || nx >= cols || cost + risk[ny][nx] >= best[ny][nx]) continue;
                best[ny][nx] = cost + risk[ny][nx];
                push(best[ny][nx], ny, nx);
            }
        }
    return 1;
}
