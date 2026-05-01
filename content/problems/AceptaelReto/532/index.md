---
title: "532 — AceptaelReto"
summary: "Solución al problema 532 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 532

```cpp

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; scanf("%d",&n);
    while(n--){
        int a,b; scanf("%d %d",&a,&b);
        printf("%d\n",abs(a-b));
    }
    return 0;
}
```
