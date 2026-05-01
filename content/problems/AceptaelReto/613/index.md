---
title: "613 — AceptaelReto"
summary: "Solución al problema 613 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 613

```cpp

#include <bits/stdc++.h>
using namespace std;

int main() {
    int num;
    while(scanf("%d",&num)==1){
        int ones = 0, c =-1;
        while(c!=0){
            if(c==-1) c=0;
            c = (c*10+1)%num;
            ones++;
        }
        printf("%d\n",ones);
    }
    return 0;
}
```
