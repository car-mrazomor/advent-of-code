#include <stdio.h>
#include <string.h>

#define MAX 8192

int main(void) {
    static long value[MAX];
    static int order[MAX];
    int n = 0;
    while (scanf("%ld", &value[n]) == 1) order[n] = n, n++;
    for (int i = 0; i < n; i++) {
        int pos = 0;
        while (order[pos] != i) pos++;
        long shift = value[i] % (n - 1);
        int target = (int)((pos + shift) % (n - 1));
        if (target < 0) target += n - 1;
        if (target > pos) memmove(&order[pos], &order[pos + 1], (size_t)(target - pos) * sizeof(int));
        else memmove(&order[target + 1], &order[target], (size_t)(pos - target) * sizeof(int));
        order[target] = i;
    }
    int zero = 0;
    while (value[order[zero]] != 0) zero++;
    long sum = 0;
    for (int k = 1000; k <= 3000; k += 1000) sum += value[order[(zero + k) % n]];
    printf("%ld\n", sum);
    return 0;
}
