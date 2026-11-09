#include <stdio.h>
#include <string.h>

static unsigned long long memory[1 << 17];

int main(void) {
    char line[128], mask[40];
    unsigned long long ones = 0, zeros = ~0ULL, address, value;
    while (fgets(line, sizeof line, stdin)) {
        if (sscanf(line, "mask = %36s", mask) == 1) {
            ones = 0, zeros = ~0ULL;
            for (int i = 0; i < 36; i++) {
                unsigned long long bit = 1ULL << (35 - i);
                if (mask[i] == '1') ones |= bit;
                if (mask[i] == '0') zeros &= ~bit;
            }
        } else if (sscanf(line, "mem[%llu] = %llu", &address, &value) == 2) {
            memory[address] = (value | ones) & zeros;
        }
    }
    unsigned long long sum = 0;
    for (size_t i = 0; i < sizeof memory / sizeof *memory; i++) sum += memory[i];
    printf("%llu\n", sum);
    return 0;
}
