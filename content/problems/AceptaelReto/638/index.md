---
title: "638 — AceptaelReto"
summary: "Solución al problema 638 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 638

```cpp

#include <bits/stdc++.h>
using namespace std;

int main(){
    int cases; scanf("%d",&cases);
    while(cases--){
        int c,n; scanf("%d %d",&c,&n);
        int maximo =n/(c-1)+n;
        int minimo = maximo;
        while(((minimo-1)-((minimo-1)/c))==n)
            minimo--;
        printf("%d %d\n", minimo,maximo);
    }
    return 0;
}
```
