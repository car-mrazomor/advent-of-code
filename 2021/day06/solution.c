#include <stdio.h>

int main(void) {
    long timers[9] = {0};
    int t;
    while (scanf("%d,", &t) == 1) timers[t]++;
    for (int day = 0; day < 80; day++) {
        long spawning = timers[0];
        for (int i = 0; i < 8; i++) timers[i] = timers[i + 1];
        timers[6] += spawning;
        timers[8] = spawning;
    }
    long total = 0;
    for (int i = 0; i < 9; i++) total += timers[i];
    printf("%ld\n", total);
    return 0;
}
