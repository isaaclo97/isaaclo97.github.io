---
title: "615 — AceptaelReto"
summary: "Solución al problema 615 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 615

```cpp

#include <bits/stdc++.h>
using namespace std;

int main() {
    int cases; scanf("%d",&cases);
    while(cases--){
        int n,f,t; scanf("%d %d %d",&n,&f,&t);
        printf("%d\n",(t%(n+1))*f);
    }
    return 0;
}
```
