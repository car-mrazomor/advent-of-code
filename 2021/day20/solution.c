#include <stdio.h>
#include <string.h>

#define PAD 4
#define MAX 256

static char rule[600], image[MAX][MAX], next[MAX][MAX];

int main(void) {
    scanf("%599s", rule);
    char line[MAX];
    int rows = 0, cols = 0;
    while (scanf("%255s", line) == 1) {
        cols = (int)strlen(line);
        for (int x = 0; x < cols; x++) image[rows + PAD][x + PAD] = line[x] == '#';
        rows++;
    }
    int size_y = rows + 2 * PAD, size_x = cols + 2 * PAD, outside = 0;
    for (int step = 0; step < 2; step++) {
        for (int y = 0; y < size_y; y++)
            for (int x = 0; x < size_x; x++) {
                int index = 0;
                for (int dy = -1; dy <= 1; dy++)
                    for (int dx = -1; dx <= 1; dx++) {
                        int ny = y + dy, nx = x + dx;
                        int lit = ny < 0 || ny >= size_y || nx < 0 || nx >= size_x ? outside : image[ny][nx];
                        index = index * 2 + lit;
                    }
                next[y][x] = rule[index] == '#';
            }
        outside = rule[outside ? 511 : 0] == '#';
        memcpy(image, next, sizeof image);
    }
    int lit = 0;
    for (int y = 0; y < size_y; y++)
        for (int x = 0; x < size_x; x++) lit += image[y][x];
    printf("%d\n", lit);
    return 0;
}
