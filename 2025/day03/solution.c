#include <stdio.h>
#include <string.h>

static long largest(const char *bank, int picks) {
    int n = (int)strlen(bank), from = 0;
    long value = 0;
    for (int left = picks; left > 0; left--) {
        int best = from;
        for (int i = from; i <= n - left; i++)
            if (bank[i] > bank[best]) best = i;
        value = value * 10 + bank[best] - '0';
        from = best + 1;
    }
    return value;
}

int main(void) {
    char bank[256];
    long two = 0, twelve = 0;
    while (scanf("%255s", bank) == 1) two += largest(bank, 2), twelve += largest(bank, 12);
    printf("%ld\n%ld\n", two, twelve);
    return 0;
}
