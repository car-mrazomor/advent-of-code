#include <stdio.h>
#include <stdlib.h>

#ifndef STEPS
#define STEPS 1000
#endif

int main(void) {
    long pos[4][3], vel[4][3] = {{0}};
    for (int i = 0; i < 4; i++)
        scanf(" <x=%ld, y=%ld, z=%ld>", &pos[i][0], &pos[i][1], &pos[i][2]);
    for (int step = 0; step < STEPS; step++) {
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                for (int k = 0; k < 3; k++)
                    vel[i][k] += (pos[j][k] > pos[i][k]) - (pos[j][k] < pos[i][k]);
        for (int i = 0; i < 4; i++)
            for (int k = 0; k < 3; k++) pos[i][k] += vel[i][k];
    }
    long total = 0;
    for (int i = 0; i < 4; i++) {
        long pot = 0, kin = 0;
        for (int k = 0; k < 3; k++) pot += labs(pos[i][k]), kin += labs(vel[i][k]);
        total += pot * kin;
    }
    printf("%ld\n", total);
    return 0;
}
