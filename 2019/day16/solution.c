#include <stdio.h>
#include <stdlib.h>

int main(void) {
    static int a[1 << 16], b[1 << 16];
    int n = 0, c;
    while ((c = getchar()) != EOF)
        if (c >= '0' && c <= '9') a[n++] = c - '0';
    static const int base[4] = {0, 1, 0, -1};
    for (int phase = 0; phase < 100; phase++) {
        for (int i = 0; i < n; i++) {
            long sum = 0;
            for (int j = i; j < n; j++) sum += a[j] * base[((j + 1) / (i + 1)) % 4];
            b[i] = abs((int)(sum % 10));
        }
        for (int i = 0; i < n; i++) a[i] = b[i];
    }
    for (int i = 0; i < 8; i++) printf("%d", a[i]);
    printf("\n");
    return 0;
}
