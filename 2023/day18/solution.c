#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char dir;
    long steps, x = 0, y = 0, twice_area = 0, perimeter = 0;
    char color[16];
    while (scanf(" %c %ld %15s", &dir, &steps, color) == 3) {
        long nx = x, ny = y;
        if (dir == 'R') nx += steps;
        if (dir == 'L') nx -= steps;
        if (dir == 'U') ny -= steps;
        if (dir == 'D') ny += steps;
        twice_area += x * ny - nx * y;
        perimeter += steps;
        x = nx, y = ny;
    }
    printf("%ld\n", labs(twice_area) / 2 + perimeter / 2 + 1);
    return 0;
}
