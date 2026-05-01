---
title: "664 — AceptaelReto"
summary: "Solución al problema 664 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 664

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    int carriles,cases;
    while(scanf("%d",&cases) == 1 && cases!=0){
        int maxCarriles, res = 0x3f3f3f3f,aux;
        for(int i=0; i<cases;i++) {
            scanf("%d", &carriles);
            maxCarriles = 0;
            for (int j = 0; j < carriles; j++) {
                scanf("%d",&aux);
                maxCarriles = max(maxCarriles,aux);
            }
            res = min(res,maxCarriles);
        }
        printf("%d\n", res);
    }
    return 0;
}
```
