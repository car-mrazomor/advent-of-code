#include <stdio.h>

#ifndef PREAMBLE
#define PREAMBLE 25
#endif

int main(void) {
    static long nums[4096];
    int n = 0;
    while (scanf("%ld", &nums[n]) == 1) n++;
    for (int i = PREAMBLE; i < n; i++) {
        int found = 0;
        for (int a = i - PREAMBLE; a < i && !found; a++)
            for (int b = a + 1; b < i && !found; b++)
                found = nums[a] != nums[b] && nums[a] + nums[b] == nums[i];
        if (!found) {
            printf("%ld\n", nums[i]);
            return 0;
        }
    }
    return 1;
}
