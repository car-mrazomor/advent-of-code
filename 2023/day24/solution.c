#include <stdio.h>

#ifndef LOW
#define LOW 200000000000000.0L
#define HIGH 400000000000000.0L
#endif

static long double px[512], py[512], vx[512], vy[512];

int main(void) {
    int n = 0;
    long double pz, vz;
    while (scanf("%Lf, %Lf, %Lf @ %Lf, %Lf, %Lf", &px[n], &py[n], &pz, &vx[n], &vy[n], &vz) == 6) n++;
    int count = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            long double det = vx[i] * vy[j] - vy[i] * vx[j];
            if (det == 0) continue;
            long double t = ((px[j] - px[i]) * vy[j] - (py[j] - py[i]) * vx[j]) / det;
            long double s = ((px[j] - px[i]) * vy[i] - (py[j] - py[i]) * vx[i]) / det;
            if (t < 0 || s < 0) continue;
            long double x = px[i] + vx[i] * t, y = py[i] + vy[i] * t;
            count += x >= LOW && x <= HIGH && y >= LOW && y <= HIGH;
        }
    printf("%d\n", count);
    return 0;
}
