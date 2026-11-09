#include <stdio.h>

int main(void) {
    char pass[16];
    int taken[1024] = {0}, highest = 0;
    while (scanf("%15s", pass) == 1) {
        int id = 0;
        for (int i = 0; pass[i]; i++) id = id * 2 + (pass[i] == 'B' || pass[i] == 'R');
        taken[id] = 1;
        if (id > highest) highest = id;
    }
    printf("%d\n", highest);
    for (int id = 1; id < 1023; id++)
        if (!taken[id] && taken[id - 1] && taken[id + 1]) printf("%d\n", id);
    return 0;
}
