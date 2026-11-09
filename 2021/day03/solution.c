#include <stdio.h>
#include <string.h>

int main(void) {
    char line[64];
    int ones[64] = {0}, lines = 0, width = 0;
    while (scanf("%63s", line) == 1) {
        width = (int)strlen(line);
        for (int i = 0; i < width; i++) ones[i] += line[i] == '1';
        lines++;
    }
    long gamma = 0, epsilon = 0;
    for (int i = 0; i < width; i++) {
        int common = ones[i] * 2 > lines;
        gamma = gamma * 2 + common;
        epsilon = epsilon * 2 + !common;
    }
    printf("%ld\n", gamma * epsilon);
    return 0;
}
