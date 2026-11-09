#include <stdio.h>

#ifndef WIDE
#define WIDE 101
#define TALL 103
#endif

int main(void) {
    long px, py, vx, vy, quadrant[4] = {0};
    while (scanf(" p=%ld,%ld v=%ld,%ld", &px, &py, &vx, &vy) == 4) {
        long x = ((px + vx * 100) % WIDE + WIDE) % WIDE, y = ((py + vy * 100) % TALL + TALL) % TALL;
        if (x == WIDE / 2 || y == TALL / 2) continue;
        quadrant[(x > WIDE / 2) + 2 * (y > TALL / 2)]++;
    }
    printf("%ld\n", quadrant[0] * quadrant[1] * quadrant[2] * quadrant[3]);
    return 0;
}
