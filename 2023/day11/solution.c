#include <stdio.h>
#include <string.h>

static char map[160][160];

int main(void) {
    int rows = 0;
    while (scanf("%159s", map[rows]) == 1) rows++;
    int cols = (int)strlen(map[0]);
    long row_pos[160], col_pos[160], gx[1024], gy[1024];
    int n = 0;
    for (int y = 0, at = 0; y < rows; y++) {
        row_pos[y] = at++;
        if (!strchr(map[y], '#')) at++;
    }
    for (int x = 0, at = 0; x < cols; x++) {
        int empty = 1;
        for (int y = 0; y < rows; y++) empty &= map[y][x] != '#';
        col_pos[x] = at++;
        if (empty) at++;
    }
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++)
            if (map[y][x] == '#') gx[n] = col_pos[x], gy[n++] = row_pos[y];
    long total = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) total += (gx[i] > gx[j] ? gx[i] - gx[j] : gx[j] - gx[i]) + (gy[j] - gy[i]);
    printf("%ld\n", total);
    return 0;
}
