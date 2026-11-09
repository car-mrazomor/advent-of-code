#include <stdio.h>
#include <string.h>

#define ROCKS 2022
#define HEIGHT (ROCKS * 4 + 16)

static unsigned char chamber[HEIGHT];
static const unsigned char shapes[5][4] = {
    {0x1e, 0, 0, 0}, {0x08, 0x1c, 0x08, 0}, {0x1c, 0x04, 0x04, 0}, {0x10, 0x10, 0x10, 0x10}, {0x18, 0x18, 0, 0}};

static int fits(const unsigned char *rock, int y) {
    for (int i = 0; i < 4; i++)
        if (rock[i] && (y + i < 0 || (chamber[y + i] & rock[i]))) return 0;
    return 1;
}

int main(void) {
    static char jets[16384];
    scanf("%16383s", jets);
    int njets = (int)strlen(jets), jet = 0, top = 0;
    for (int n = 0; n < ROCKS; n++) {
        unsigned char rock[4];
        memcpy(rock, shapes[n % 5], 4);
        int y = top + 3;
        for (;;) {
            unsigned char moved[4];
            int ok = 1;
            for (int i = 0; i < 4; i++) {
                if (jets[jet] == '<') {
                    if (rock[i] & 0x40) ok = 0;
                    moved[i] = rock[i] << 1;
                } else {
                    if (rock[i] & 0x01) ok = 0;
                    moved[i] = rock[i] >> 1;
                }
            }
            jet = (jet + 1) % njets;
            if (ok && fits(moved, y)) memcpy(rock, moved, 4);
            if (!fits(rock, y - 1)) break;
            y--;
        }
        for (int i = 0; i < 4; i++)
            if (rock[i]) {
                chamber[y + i] |= rock[i];
                if (y + i + 1 > top) top = y + i + 1;
            }
    }
    printf("%d\n", top);
    return 0;
}
