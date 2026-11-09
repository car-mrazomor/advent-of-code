#include <stdio.h>
#include <string.h>

static int left[26 * 26 * 26], right[26 * 26 * 26];

static int code(const char *s) { return (s[0] - 'A') * 676 + (s[1] - 'A') * 26 + (s[2] - 'A'); }

int main(void) {
    static char moves[1024];
    char a[4], b[4], c[4];
    scanf("%1023s", moves);
    while (scanf(" %3s = (%3s, %3s)", a, b, c) == 3) left[code(a)] = code(b), right[code(a)] = code(c);
    int at = 0, goal = code("ZZZ"), steps = 0, n = (int)strlen(moves);
    while (at != goal) at = moves[steps++ % n] == 'L' ? left[at] : right[at];
    printf("%d\n", steps);
    return 0;
}
