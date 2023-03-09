#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void seqsearch(int n, vector<int> S, int x, int& location) {
    location = 0;

    for (int i = 1; i <= n; i++) {
        if (x == S[i]) {
            location = i;
            break;
        }
    }
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> S(n+1);
    for (int i = 1; i <= n; i++)
        scanf("%d", &S[i]);
    while (m--) {
        int x, location;
        scanf("%d", &x);
        seqsearch(n, S, x, location);
        if (location > 0)
            printf("%d is in %d.\n", x, location);
        else
            printf("%d is not in S.\n", x);
    }
}