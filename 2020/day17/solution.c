#include <stdio.h>
#include <string.h>

#define N 32

static char cube[N][N][N], next[N][N][N];

int main(void) {
    char line[64];
    int y = 0;
    while (scanf("%63s", line) == 1) {
        for (int x = 0; line[x]; x++) cube[N / 2][N / 2 - 4 + y][N / 2 - 4 + x] = line[x] == '#';
        y++;
    }
    for (int cycle = 0; cycle < 6; cycle++) {
        for (int z = 1; z < N - 1; z++)
            for (int y2 = 1; y2 < N - 1; y2++)
                for (int x = 1; x < N - 1; x++) {
                    int around = -cube[z][y2][x];
                    for (int dz = -1; dz <= 1; dz++)
                        for (int dy = -1; dy <= 1; dy++)
                            for (int dx = -1; dx <= 1; dx++) around += cube[z + dz][y2 + dy][x + dx];
                    next[z][y2][x] = around == 3 || (cube[z][y2][x] && around == 2);
                }
        memcpy(cube, next, sizeof cube);
    }
    int active = 0;
    for (int i = 0; i < N * N * N; i++) active += ((char *)cube)[i];
    printf("%d\n", active);
    return 0;
}
