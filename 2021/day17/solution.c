#include <stdio.h>

int main(void) {
    int x1, x2, y1, y2, best = 0;
    scanf("target area: x=%d..%d, y=%d..%d", &x1, &x2, &y1, &y2);
    for (int vx0 = 1; vx0 <= x2; vx0++)
        for (int vy0 = y1; vy0 <= -y1; vy0++) {
            int x = 0, y = 0, vx = vx0, vy = vy0, top = 0;
            while (x <= x2 && y >= y1) {
                x += vx, y += vy;
                vx -= vx > 0, vy--;
                if (y > top) top = y;
                if (x >= x1 && x <= x2 && y >= y1 && y <= y2) {
                    if (top > best) best = top;
                    break;
                }
            }
        }
    printf("%d\n", best);
    return 0;
}
