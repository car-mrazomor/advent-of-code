#include <stdio.h>
#include <string.h>

int main(void) {
    char command[16];
    long amount, x = 0, depth = 0, aim = 0, deep = 0;
    while (scanf("%15s %ld", command, &amount) == 2) {
        if (strcmp(command, "forward") == 0) x += amount, deep += aim * amount;
        else if (strcmp(command, "down") == 0) depth += amount, aim += amount;
        else depth -= amount, aim -= amount;
    }
    printf("%ld\n%ld\n", x * depth, x * deep);
    return 0;
}
