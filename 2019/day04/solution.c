#include <stdio.h>

static int valid(int n) {
    int digits[6], pair = 0;
    for (int i = 5; i >= 0; i--, n /= 10) digits[i] = n % 10;
    for (int i = 1; i < 6; i++) {
        if (digits[i] < digits[i - 1]) return 0;
        if (digits[i] == digits[i - 1]) pair = 1;
    }
    return pair;
}

int main(void) {
    int lo, hi, count = 0;
    scanf("%d-%d", &lo, &hi);
    for (int n = lo; n <= hi; n++) count += valid(n);
    printf("%d\n", count);
    return 0;
}
