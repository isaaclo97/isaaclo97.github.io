---
title: "694 — UVA"
summary: "Solución al problema 694 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 694

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main()
{
    long long A,L,cont,caso=1;
    while(scanf("%lld%lld",&A,&L)==2 && (A>-1 || L>-1)){
        cout<<"Case "<<caso++<<": A = "<<A<<", limit = "<<L<<", number of terms = ";
        cont=0;
        while(A<=L && A!=1){
            if(A%2==0) A/=2;
            else A=3*A+1;
            cont++;
        }
        if(A==1) cont++;
        cout<<cont<<'\n';
    }
    return 0;
}
```
