---
title: "545 — AceptaelReto"
summary: "Solución al problema 545 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 545

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    int l,c;
    while(scanf("%d %d",&l,&c)==2){
        int res = 0x3f3f3f3f;
        for(int i=0; i<c;i++){
            int a,b; scanf("%d %d",&a,&b);
            if(a<0) continue;
            res = min(res,l/b+a);
        }
        printf("%d\n",res);
    }
    return 0;
}
```
