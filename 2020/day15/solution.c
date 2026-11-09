#include <stdio.h>

#define TURNS 2020

int main(void) {
    static int last[TURNS + 1];
    int value, turn = 0, previous = -1;
    while (scanf("%d,", &value) == 1) {
        if (previous >= 0) last[previous] = turn;
        previous = value;
        turn++;
    }
    for (; turn < TURNS; turn++) {
        int next = last[previous] ? turn - last[previous] : 0;
        last[previous] = turn;
        previous = next;
    }
    printf("%d\n", previous);
    return 0;
}
