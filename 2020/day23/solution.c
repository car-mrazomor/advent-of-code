#include <stdio.h>

int main(void) {
    char labels[16];
    scanf("%15s", labels);
    int next[10], n = 9;
    for (int i = 0; i < n; i++) next[labels[i] - '0'] = labels[(i + 1) % n] - '0';
    int current = labels[0] - '0';
    for (int move = 0; move < 100; move++) {
        int a = next[current], b = next[a], c = next[b];
        int dest = current;
        do dest = dest == 1 ? n : dest - 1;
        while (dest == a || dest == b || dest == c);
        next[current] = next[c];
        next[c] = next[dest];
        next[dest] = a;
        current = next[current];
    }
    for (int cup = next[1]; cup != 1; cup = next[cup]) printf("%d", cup);
    printf("\n");
    return 0;
}
