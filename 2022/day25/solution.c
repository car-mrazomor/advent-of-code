#include <stdio.h>
#include <string.h>

int main(void) {
    char line[64];
    long sum = 0;
    while (scanf("%63s", line) == 1) {
        long value = 0;
        for (char *c = line; *c; c++) value = value * 5 + (*c == '=' ? -2 : *c == '-' ? -1 : *c - '0');
        sum += value;
    }
    char out[64];
    int n = 0;
    do {
        int digit = (int)(((sum % 5) + 5) % 5);
        out[n++] = "012=-"[digit];
        sum = (sum + 2) / 5;
    } while (sum);
    while (n--) putchar(out[n]);
    putchar('\n');
    return 0;
}
