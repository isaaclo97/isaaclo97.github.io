---
title: "583 — AceptaelReto"
summary: "Solución al problema 583 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 583

```cpp

#include <bits/stdc++.h>
using namespace std;

int main(){
    int cases; scanf("%d",&cases);
    while(cases--){
        long long int comprometedora, otra;
        scanf("%lld %lld",&comprometedora,&otra);
        double percentage = ((comprometedora-(comprometedora+otra)/2) * 100)/((comprometedora+otra)/2);
        printf("%d\n",(long long int)(percentage));
    }
    return 0;
}
```
