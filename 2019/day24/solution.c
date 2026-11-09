#include <stdio.h>
#include <stdlib.h>

int main(void) {
    unsigned state = 0;
    int i = 0, c;
    while ((c = getchar()) != EOF && i < 25) {
        if (c == '#') state |= 1u << i++;
        else if (c == '.') i++;
    }
    unsigned char *seen = calloc(1 << 22, 1);
    while (!(seen[state >> 3] & (1 << (state & 7)))) {
        seen[state >> 3] |= 1 << (state & 7);
        unsigned next = 0;
        for (int y = 0; y < 5; y++)
            for (int x = 0; x < 5; x++) {
                int around = (y > 0 && (state >> ((y - 1) * 5 + x) & 1)) + (y < 4 && (state >> ((y + 1) * 5 + x) & 1)) +
                             (x > 0 && (state >> (y * 5 + x - 1) & 1)) + (x < 4 && (state >> (y * 5 + x + 1) & 1));
                int bug = state >> (y * 5 + x) & 1;
                if (around == 1 || (!bug && around == 2)) next |= 1u << (y * 5 + x);
            }
        state = next;
    }
    printf("%u\n", state);
    free(seen);
    return 0;
}
