---
title: "540 — AceptaelReto"
summary: "Solución al problema 540 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 540

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    int cases; scanf("%d",&cases);
    while(cases--){
        long long int n,m,p,d; scanf("%lld %lld %lld %lld",&n,&m,&p,&d);
        printf("%lld %lld\n",m*p+d,n*m+m*p+d);
    }
    return 0;
}
```
