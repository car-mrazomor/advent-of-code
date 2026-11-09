#include <stdio.h>

static char cube[32][32][32];

int main(void) {
    int x, y, z, area = 0;
    while (scanf("%d,%d,%d", &x, &y, &z) == 3) cube[x + 1][y + 1][z + 1] = 1;
    for (x = 1; x < 31; x++)
        for (y = 1; y < 31; y++)
            for (z = 1; z < 31; z++)
                if (cube[x][y][z])
                    area += !cube[x + 1][y][z] + !cube[x - 1][y][z] + !cube[x][y + 1][z] + !cube[x][y - 1][z] +
                            !cube[x][y][z + 1] + !cube[x][y][z - 1];
    printf("%d\n", area);
    return 0;
}
