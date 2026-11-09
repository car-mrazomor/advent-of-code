#include <stdio.h>

static int energy[10][10];

static int flash(int y, int x) {
    if (y < 0 || y > 9 || x < 0 || x > 9 || energy[y][x] > 9 || ++energy[y][x] <= 9) return 0;
    int count = 1;
    for (int dy = -1; dy <= 1; dy++)
        for (int dx = -1; dx <= 1; dx++)
            if (dy || dx) count += flash(y + dy, x + dx);
    return count;
}

int main(void) {
    char row[16];
    for (int y = 0; y < 10 && scanf("%15s", row) == 1; y++)
        for (int x = 0; x < 10; x++) energy[y][x] = row[x] - '0';
    int total = 0;
    for (int step = 0; step < 100; step++) {
        for (int y = 0; y < 10; y++)
            for (int x = 0; x < 10; x++) total += flash(y, x);
        for (int y = 0; y < 10; y++)
            for (int x = 0; x < 10; x++)
                if (energy[y][x] > 9) energy[y][x] = 0;
    }
    printf("%d\n", total);
    return 0;
}
