#include <stdio.h>

int main(void) {
    int pos[2], score[2] = {0}, die = 0, rolls = 0;
    scanf("Player 1 starting position: %d\nPlayer 2 starting position: %d", &pos[0], &pos[1]);
    for (int player = 0;; player ^= 1) {
        int move = 0;
        for (int i = 0; i < 3; i++) move += die % 100 + 1, die++;
        rolls += 3;
        pos[player] = (pos[player] + move - 1) % 10 + 1;
        score[player] += pos[player];
        if (score[player] >= 1000) {
            printf("%d\n", score[player ^ 1] * rolls);
            return 0;
        }
    }
}
