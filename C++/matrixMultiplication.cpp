#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<vector<int>> matrix_t;

void matrixmult(int n, matrix_t A, matrix_t B, matrix_t& C) {
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            for (int k = 1; k <= n; k++)
                C[i][j] += A[i][k] * B[k][j];
}

void matrixread(int n, matrix_t& M) {
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            scanf("%d", &M[i][j]);
}

int main() {
    int n;
    scanf("%d", &n);

    matrix_t A(n+1, vector<int>(n+1));
    matrixread(n, A);
    matrix_t B(n+1, vector<int>(n+1));
    matrixread(n, B);
    matrix_t C(n+1, vector<int>(n+1));
    matrixmult(n, A, B, C);

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (j < n)
                printf("%d ", C[i][j]);
            else
                printf("%d\n", C[i][j]);
}