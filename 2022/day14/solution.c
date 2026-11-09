#include <stdio.h>

static char cave[200][1000];

int main(void) {
    char line[4096];
    int lowest = 0;
    while (fgets(line, sizeof line, stdin)) {
        int x, y, px = -1, py = -1, used;
        char *p = line;
        while (sscanf(p, "%d,%d%n", &x, &y, &used) == 2) {
            if (px >= 0)
                for (int i = px < x ? px : x; i <= (px > x ? px : x); i++)
                    for (int j = py < y ? py : y; j <= (py > y ? py : y); j++) cave[j][i] = 1;
            if (y > lowest) lowest = y;
            px = x, py = y;
            p += used;
            while (*p == ' ' || *p == '-' || *p == '>') p++;
        }
    }
    int resting = 0;
    for (;;) {
        int x = 500, y = 0;
        for (;;) {
            if (y > lowest) {
                printf("%d\n", resting);
                return 0;
            }
            if (!cave[y + 1][x]) y++;
            else if (!cave[y + 1][x - 1]) y++, x--;
            else if (!cave[y + 1][x + 1]) y++, x++;
            else break;
        }
        cave[y][x] = 1;
        resting++;
    }
}
