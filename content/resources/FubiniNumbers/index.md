---
title: "Algoritmo de FubiniNumbers."
type: page
---

```cpp
//0,1,1,3,13,75,541,4683,47293,545835

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define nmax 3100
#define nnum 46337
LL num[nmax][nmax], fac[nmax];
void init() {
    int i, j;
    for (i = 1, fac[0] = 1; i < nmax; i++) {
        fac[i] = fac[i - 1] * i % nnum;
    }
    for (i = 1; i < nmax; i++) {
        num[i][1] = 1;
        num[i][0] = 0;
    }
    for (i = 2; i < nmax; i++) {
        for (j = 1; j < nmax; j++) {
            if (i == j) {
                num[i][i] = 1;
            } else {
                num[i][j] = (num[i - 1][j - 1] + num[i - 1][j] * j) % nnum;
            }
        }
    }
}
int main() {
    ofstream myfile;
    myfile.open ("example.txt");
    init();
    int  N=0, i;
    LL res;
    while (N!=3050) {
            for (i = 1, res = 0; i <= N; i++) {
                res += num[N][i] * fac[i];
                res %= nnum;
            }
            myfile<<res<<",";
            printf("%I64d\n", res);
            N++;
        }
    myfile.close();
 return 0; }
```
