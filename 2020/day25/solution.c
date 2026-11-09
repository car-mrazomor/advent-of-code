#include <stdio.h>

#define MOD 20201227

int main(void) {
    long card, door, value = 1, key = 1;
    scanf("%ld %ld", &card, &door);
    while (value != card) {
        value = value * 7 % MOD;
        key = key * door % MOD;
    }
    printf("%ld\n", key);
    return 0;
}
