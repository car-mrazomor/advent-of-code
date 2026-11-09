#include <stdio.h>
#include <string.h>

#ifndef DECK
#define DECK 10007
#endif
#ifndef CARD
#define CARD 2019
#endif

int main(void) {
    long pos = CARD, n;
    char line[64];
    while (fgets(line, sizeof line, stdin)) {
        if (strncmp(line, "deal into", 9) == 0) pos = DECK - 1 - pos;
        else if (sscanf(line, "cut %ld", &n) == 1) pos = ((pos - n) % DECK + DECK) % DECK;
        else if (sscanf(line, "deal with increment %ld", &n) == 1) pos = pos * n % DECK;
    }
    printf("%ld\n", pos);
    return 0;
}
