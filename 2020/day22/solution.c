#include <stdio.h>

#define SIZE 1024

int main(void) {
    int deck[2][SIZE], head[2] = {0}, tail[2] = {0}, player = -1, card;
    char line[64];
    while (fgets(line, sizeof line, stdin)) {
        if (line[0] == 'P') player++;
        else if (sscanf(line, "%d", &card) == 1) deck[player][tail[player]++ % SIZE] = card;
    }
    while (head[0] != tail[0] && head[1] != tail[1]) {
        int a = deck[0][head[0]++ % SIZE], b = deck[1][head[1]++ % SIZE];
        int winner = a > b ? 0 : 1;
        deck[winner][tail[winner]++ % SIZE] = winner ? b : a;
        deck[winner][tail[winner]++ % SIZE] = winner ? a : b;
    }
    int winner = head[0] != tail[0] ? 0 : 1;
    long score = 0;
    for (int i = head[winner], n = tail[winner] - head[winner]; i < tail[winner]; i++, n--) score += (long)deck[winner][i % SIZE] * n;
    printf("%ld\n", score);
    return 0;
}
