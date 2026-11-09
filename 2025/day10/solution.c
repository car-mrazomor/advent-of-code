#include <stdio.h>
#include <string.h>

int main(void) {
    char line[1024];
    long total = 0;
    while (fgets(line, sizeof line, stdin)) {
        char *open = strchr(line, '['), *close = strchr(line, ']');
        if (!open || !close) continue;
        unsigned target = 0, buttons[32];
        int n = 0;
        for (char *c = open + 1; c < close; c++)
            if (*c == '#') target |= 1u << (c - open - 1);
        for (char *p = close; (p = strchr(p, '(')) != NULL && p < strchr(line, '{');) {
            unsigned mask = 0;
            int light, used;
            p++;
            while (sscanf(p, "%d%n", &light, &used) == 1) {
                mask |= 1u << light;
                p += used;
                if (*p == ',') p++;
            }
            buttons[n++] = mask;
        }
        int best = n + 1;
        for (unsigned subset = 0; subset < 1u << n; subset++) {
            unsigned lights = 0;
            for (int b = 0; b < n; b++)
                if (subset >> b & 1) lights ^= buttons[b];
            if (lights == target && __builtin_popcount(subset) < best) best = __builtin_popcount(subset);
        }
        total += best;
    }
    printf("%ld\n", total);
    return 0;
}
