#include <stdio.h>
#include <string.h>

static const char *words[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

static int digit_at(const char *s, int spelled) {
    if (*s >= '0' && *s <= '9') return *s - '0';
    if (spelled)
        for (int d = 0; d < 9; d++)
            if (strncmp(s, words[d], strlen(words[d])) == 0) return d + 1;
    return -1;
}

int main(void) {
    char line[256];
    long sums[2] = {0, 0};
    while (scanf("%255s", line) == 1)
        for (int spelled = 0; spelled < 2; spelled++) {
            int first = -1, last = -1;
            for (char *p = line; *p; p++) {
                int d = digit_at(p, spelled);
                if (d < 0) continue;
                if (first < 0) first = d;
                last = d;
            }
            if (first >= 0) sums[spelled] += first * 10 + last;
        }
    printf("%ld\n%ld\n", sums[0], sums[1]);
    return 0;
}
