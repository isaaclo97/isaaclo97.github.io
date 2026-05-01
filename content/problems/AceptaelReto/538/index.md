---
title: "538 — AceptaelReto"
summary: "Solución al problema 538 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 538

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    while(scanf("%d %d",&n,&m)==2 && (n!=0 || m!=0)){
        if(n>=m) printf("CUERDO\n");
        else printf("SENIL\n");
    }
    return 0;
}
```
