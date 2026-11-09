#include <stdio.h>

int main(void) {
    static long mem[4096];
    int n = 0;
    while (scanf("%ld,", &mem[n]) == 1) n++;
    if (n > 12) { mem[1] = 12; mem[2] = 2; }
    for (int ip = 0; mem[ip] != 99; ip += 4) {
        long a = mem[mem[ip + 1]], b = mem[mem[ip + 2]];
        mem[mem[ip + 3]] = mem[ip] == 1 ? a + b : a * b;
    }
    printf("%ld\n", mem[0]);
    return 0;
}
