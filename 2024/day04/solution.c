#include <stdio.h>
#include <string.h>

static char grid[160][160];

int main(void) {
    int rows = 0;
    while (scanf("%159s", grid[rows]) == 1) rows++;
    int cols = (int)strlen(grid[0]), count = 0;
    static const char word[] = "XMAS";
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++)
            for (int dy = -1; dy <= 1; dy++)
                for (int dx = -1; dx <= 1; dx++) {
                    if (!dy && !dx) continue;
                    int k = 0;
                    while (k < 4) {
                        int ny = y + dy * k, nx = x + dx * k;
                        if (ny < 0 || ny >= rows || nx < 0 || nx >= cols || grid[ny][nx] != word[k]) break;
                        k++;
                    }
                    count += k == 4;
                }
    printf("%d\n", count);
    return 0;
}
