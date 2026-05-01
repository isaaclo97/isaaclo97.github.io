---
title: "Algoritmo de Knapsack Problem Dynamic Programming."
type: page
---

```cpp
/*
0/1 Knapsack Problem Dynamic Programming
0/1 solo se puede coger uno no mas

val w   0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
(0) 0 | 0   0   0   0   0   0   0   0
(1) 1 | 0   1   1   1   1   1   1   1
(4) 3 | 0   1   1   4   5   5   5   5
(5) 4 | 0   1   1   4   5   6   6   9
(7) 5 | 0   1   1   4   5   7   8   9

Teniendo un peso total, coger los objetos que tengan menos peso que X con
mayor valor.
Si mi peso total es 0, lo mejor que tengo es 0.
Si mi peso total es X, lo mejor que puedo es X
Cuando hay varios nos quedamos con el max(4+T[0][0],1), volviendo atrs w veces.

Total wt = 7

wt  1 3 4 5
val 1 4 5 7

*/
/*
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int val[] = {1,4,5,7};
    int wt[] = {1,3,4,5};
    int W=7;
    int L=4;
    int K[L+1][W+1];
    for(int i=0; i <= L; i++){
        for(int j=0; j <= W; j++){
            if(i == 0 || j == 0){
                K[i][j] = 0;
                continue;
            }
            if(j - wt[i-1] >= 0)  K[i][j] = max(K[i-1][j], K[i-1][j-wt[i-1]] + val[i-1]);
            else K[i][j] = K[i-1][j];
            cout<<K[i][j]<<' ';
        }
        cout<<'\n';
    }
    cout<< K[L][W]<<'\n';

    cout<<"GET VALUES\n";

    int i = L;
    int j = W;
    while(i!=0 && j!=0)
    {
           if(K[i-1][j]==K[i][j])  i--;
           else { cout<<wt[i-1]<<"("<<val[i-1]<<")\n"; j-=wt[i]; j++; i--; }
    }
    return 0;
}
*/
```
