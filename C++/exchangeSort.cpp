#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//교환 정렬
//처음 데이터와 그 다음데이터를 비교하여,
//순서가 잘못 되어 있으면 바꾸어주고
//그렇지 않으면 처음 데이터와 다음 데이터를 비교
//마지막 바로 이전의 데이터와 마지막 데이터를 비교할 때까지 연산을 반복 수행함

void exchange(int n, vector<int>& S) {
    int temp;

    for (int i = 1; i <= n-1; i++)
        for (int j = i+1; j <= n; j++)
            if (S[i] > S[j]) {
                temp = S[i];
                S[i] = S[j];
                S[j] = temp;
            }

}

int main() {
    int n;
    scanf("%d", &n);
    vector<int> S(n+1);
    for (int i = 1; i <= n; i++)
        scanf("%d", &S[i]);
    exchange(n, S);
    for (int i = 1; i <= n; i++)
        if (i < n)
            printf("%d ", S[i]);
        else
            printf("%d\n", S[i]);
}