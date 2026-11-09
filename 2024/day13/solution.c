#include <stdio.h>

int main(void) {
    long ax, ay, bx, by, px, py, tokens = 0;
    while (scanf(" Button A: X+%ld, Y+%ld Button B: X+%ld, Y+%ld Prize: X=%ld, Y=%ld", &ax, &ay, &bx, &by, &px, &py) == 6) {
        long det = ax * by - ay * bx;
        if (det == 0) continue;
        long a = px * by - py * bx, b = ax * py - ay * px;
        if (a % det || b % det) continue;
        a /= det, b /= det;
        if (a >= 0 && b >= 0 && a <= 100 && b <= 100) tokens += 3 * a + b;
    }
    printf("%ld\n", tokens);
    return 0;
}
