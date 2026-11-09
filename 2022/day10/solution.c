#include <stdio.h>
#include <string.h>

static int cycle = 0, x = 1, total = 0;

static void tick(void) {
    cycle++;
    if (cycle % 40 == 20) total += cycle * x;
}

int main(void) {
    char op[8];
    int value;
    while (scanf("%7s", op) == 1) {
        tick();
        if (strcmp(op, "addx") == 0 && scanf("%d", &value) == 1) {
            tick();
            x += value;
        }
    }
    printf("%d\n", total);
    return 0;
}
