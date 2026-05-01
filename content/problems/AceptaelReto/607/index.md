---
title: "607 — AceptaelReto"
summary: "Solución al problema 607 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 607

```cpp

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; scanf("%d",&n);
    while(n--){
        int num; scanf("%d",&num);
        for(int i=0; i<35;i++){
            if(pow(2,i)>=num) { printf("%d\n",i); break;}
        }
    }
    return 0;
}
```
