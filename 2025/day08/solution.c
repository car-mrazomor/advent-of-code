#include <stdio.h>
#include <stdlib.h>

#ifndef CONNECT
#define CONNECT 1000
#endif

typedef struct { long dist; int a, b; } pair;

static long x[2048], y[2048], z[2048];
static int parent[2048], size[2048];

static int find(int i) { return parent[i] == i ? i : (parent[i] = find(parent[i])); }

static int by_distance(const void *p, const void *q) {
    long a = ((const pair *)p)->dist, b = ((const pair *)q)->dist;
    return (a > b) - (a < b);
}

static int by_size_desc(const void *p, const void *q) { return *(const int *)q - *(const int *)p; }

int main(void) {
    int n = 0;
    while (scanf("%ld,%ld,%ld", &x[n], &y[n], &z[n]) == 3) n++;
    long count = (long)n * (n - 1) / 2;
    pair *pairs = malloc(sizeof(pair) * (size_t)count);
    long k = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            long dx = x[i] - x[j], dy = y[i] - y[j], dz = z[i] - z[j];
            pairs[k++] = (pair){dx * dx + dy * dy + dz * dz, i, j};
        }
    qsort(pairs, (size_t)count, sizeof(pair), by_distance);
    for (int i = 0; i < n; i++) parent[i] = i, size[i] = 1;
    int circuits = n;
    for (long p = 0; p < count; p++) {
        int a = find(pairs[p].a), b = find(pairs[p].b);
        if (a != b) {
            parent[a] = b, size[b] += size[a], circuits--;
            if (circuits == 1) {
                printf("%ld\n", x[pairs[p].a] * x[pairs[p].b]);
                break;
            }
        }
        if (p + 1 == CONNECT) {
            int sizes[2048], m = 0;
            for (int i = 0; i < n; i++)
                if (find(i) == i) sizes[m++] = size[i];
            qsort(sizes, (size_t)m, sizeof(int), by_size_desc);
            printf("%ld\n", (long)sizes[0] * sizes[1] * sizes[2]);
        }
    }
    free(pairs);
    return 0;
}
