---
title: "11805 — UVA"
summary: "Solución al problema 11805 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11805

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main() {
    int T,N,K,P, ca = 1; cin>>T;
    while(T--) {
        cin>>N>>K>>P;
        int n = (K+P)%N;
        if(n==0) n =N;
        printf("Case %d: %d\n",ca++, n);
    }
    return 0;
}
```
