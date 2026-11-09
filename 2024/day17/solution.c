#include <stdio.h>

int main(void) {
    long reg[3];
    int program[64], n = 0;
    scanf(" Register A: %ld Register B: %ld Register C: %ld Program: ", &reg[0], &reg[1], &reg[2]);
    while (scanf("%d,", &program[n]) == 1) n++;
    int first = 1;
    for (int ip = 0; ip + 1 < n;) {
        int op = program[ip], lit = program[ip + 1];
        long combo = lit < 4 ? lit : reg[lit - 4];
        ip += 2;
        switch (op) {
        case 0: reg[0] >>= combo; break;
        case 1: reg[1] ^= lit; break;
        case 2: reg[1] = combo & 7; break;
        case 3: if (reg[0]) ip = lit; break;
        case 4: reg[1] ^= reg[2]; break;
        case 5: printf(first ? "%ld" : ",%ld", combo & 7), first = 0; break;
        case 6: reg[1] = reg[0] >> combo; break;
        case 7: reg[2] = reg[0] >> combo; break;
        }
    }
    printf("\n");
    return 0;
}
