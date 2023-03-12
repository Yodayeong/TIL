#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int sum(int n, vector<int> S) {
    int sum = 0;

    for (int i = 0; i <= n; i++)
        sum += S[i];

    return sum;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<int> S(n+1);
    for (int i = 1; i <= n; i++)
        scanf("%d", &S[i]);
    printf("%d", sum(n, S));
}