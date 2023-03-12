#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//이분탐색
//정렬된 리스트에서 원하는 값의 존재 여부를 찾는 알고리즘
//검사 범위에서 중간에 있는 값을 mid로 두고, 찾고자 하는 값과 비교해서 다음 검사 범위를 변경함

void binsearch(int n, vector<int> S, int x, int& location) {
    int low = 1;
    int high = n;
    while (low <= high) {
        int mid = (low + high) / 2;

        if (x == S[mid]) {
            location = mid;
            return;
        }
        else if (x < S[mid])
            high = mid - 1;
        else
            low = mid + 1;

    }
    location = 0;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> S(n+1);
    for (int i = 1; i <= n; i++)
        scanf("%d", &S[i]);
    sort(S.begin() + 1, S.end());
    while (m--) {
        int x, location;
        scanf("%d", &x);
        binsearch(n, S, x, location);
        if (location > 0)
            printf("%d is in %d.\n", x, location);
        else
            printf("%d is not in S.\n", x);
    }
}