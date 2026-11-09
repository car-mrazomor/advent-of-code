#include <stdio.h>
#include <string.h>

static char p[32][32];
static int rows, cols;

static int mirror_row(void) {
    for (int r = 1; r < rows; r++) {
        int ok = 1;
        for (int i = 0; ok && r - 1 - i >= 0 && r + i < rows; i++) ok = strcmp(p[r - 1 - i], p[r + i]) == 0;
        if (ok) return r;
    }
    return 0;
}

static int mirror_col(void) {
    for (int c = 1; c < cols; c++) {
        int ok = 1;
        for (int i = 0; ok && c - 1 - i >= 0 && c + i < cols; i++)
            for (int r = 0; r < rows; r++) ok &= p[r][c - 1 - i] == p[r][c + i];
        if (ok) return c;
    }
    return 0;
}

int main(void) {
    char line[64];
    long total = 0;
    for (;;) {
        char *got = fgets(line, sizeof line, stdin);
        if (!got || line[0] == '\n') {
            if (rows) total += 100L * mirror_row() + mirror_col();
            rows = 0;
            if (!got) break;
            continue;
        }
        line[strcspn(line, "\n")] = 0;
        strcpy(p[rows++], line);
        cols = (int)strlen(line);
    }
    printf("%ld\n", total);
    return 0;
}
