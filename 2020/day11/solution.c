#include <stdio.h>
#include <string.h>

static char grid[128][128], next[128][128];
static int rows, cols;

int main(void) {
    while (scanf("%127s", grid[rows]) == 1) rows++;
    cols = (int)strlen(grid[0]);
    for (int changed = 1; changed;) {
        changed = 0;
        for (int y = 0; y < rows; y++)
            for (int x = 0; x < cols; x++) {
                int around = 0;
                for (int dy = -1; dy <= 1; dy++)
                    for (int dx = -1; dx <= 1; dx++) {
                        int ny = y + dy, nx = x + dx;
                        if ((dy || dx) && ny >= 0 && ny < rows && nx >= 0 && nx < cols) around += grid[ny][nx] == '#';
                    }
                char c = grid[y][x];
                next[y][x] = c == 'L' && around == 0 ? '#' : c == '#' && around >= 4 ? 'L' : c;
                changed |= next[y][x] != c;
            }
        memcpy(grid, next, sizeof grid);
    }
    int occupied = 0;
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++) occupied += grid[y][x] == '#';
    printf("%d\n", occupied);
    return 0;
}
