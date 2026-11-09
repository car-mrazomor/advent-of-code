#include <stdio.h>
#include <string.h>

int main(void) {
    static char map[128][128];
    int rows = 0;
    while (scanf("%127s", map[rows]) == 1) rows++;
    int cols = (int)strlen(map[0]), risk = 0;
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols; x++) {
            char h = map[y][x];
            if ((y == 0 || map[y - 1][x] > h) && (y == rows - 1 || map[y + 1][x] > h) &&
                (x == 0 || map[y][x - 1] > h) && (x == cols - 1 || map[y][x + 1] > h))
                risk += h - '0' + 1;
        }
    printf("%d\n", risk);
    return 0;
}
