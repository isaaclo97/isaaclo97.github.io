---
title: "535 — AceptaelReto"
summary: "Solución al problema 535 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 535

```cpp

#include <bits/stdc++.h>
using namespace std;

int main(){
    int d;
    while(scanf("%d",&d)==1 && d!=0){
        int res = 0; int arr[d];
        for(int i=0; i<d;i++) scanf("%d",&arr[i]);
        for(int i=0; i<d;i++) res+=arr[d-1]-arr[i];
        printf("%d\n",res);
    }
    return 0;
}
```
