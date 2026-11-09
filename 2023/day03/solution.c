#include <ctype.h>
#include <stdio.h>
#include <string.h>

static char map[160][160];
static int rows, cols;

static int symbol(int y, int x) {
    return y >= 0 && y < rows && x >= 0 && x < cols && map[y][x] != '.' && !isdigit((unsigned char)map[y][x]);
}

int main(void) {
    while (scanf("%159s", map[rows]) == 1) rows++;
    cols = (int)strlen(map[0]);
    long sum = 0;
    for (int y = 0; y < rows; y++)
        for (int x = 0; x < cols;) {
            if (!isdigit((unsigned char)map[y][x])) {
                x++;
                continue;
            }
            int start = x, value = 0, touches = 0;
            while (x < cols && isdigit((unsigned char)map[y][x])) value = value * 10 + map[y][x++] - '0';
            for (int yy = y - 1; yy <= y + 1; yy++)
                for (int xx = start - 1; xx <= x; xx++) touches |= symbol(yy, xx);
            if (touches) sum += value;
        }
    printf("%ld\n", sum);
    return 0;
}
