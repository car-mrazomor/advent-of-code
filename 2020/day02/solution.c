#include <stdio.h>
#include <string.h>

int main(void) {
    int lo, hi, first = 0, second = 0;
    char letter, password[128];
    while (scanf("%d-%d %c: %127s", &lo, &hi, &letter, password) == 4) {
        int count = 0, len = (int)strlen(password);
        for (int i = 0; i < len; i++) count += password[i] == letter;
        first += count >= lo && count <= hi;
        second += (lo <= len && password[lo - 1] == letter) != (hi <= len && password[hi - 1] == letter);
    }
    printf("%d\n%d\n", first, second);
    return 0;
}
