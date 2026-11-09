#include <stdio.h>
#include <stdlib.h>

int main(void) {
    static char map[32768];
    int n = 0, c, size = 0;
    while ((c = getchar()) != EOF)
        if (c >= '0' && c <= '9') map[n++] = (char)(c - '0'), size += c - '0';
    int *disk = malloc(sizeof(int) * (size_t)size), len = 0;
    for (int i = 0; i < n; i++)
        for (int k = 0; k < map[i]; k++) disk[len++] = i % 2 ? -1 : i / 2;
    for (int a = 0, b = len - 1; a < b;) {
        if (disk[a] != -1) a++;
        else if (disk[b] == -1) b--;
        else disk[a++] = disk[b], disk[b--] = -1;
    }
    long checksum = 0;
    for (int i = 0; i < len && disk[i] != -1; i++) checksum += (long)i * disk[i];
    printf("%ld\n", checksum);
    free(disk);
    return 0;
}
