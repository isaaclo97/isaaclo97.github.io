---
title: "609 — AceptaelReto"
summary: "Solución al problema 609 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 609

```cpp

#include <bits/stdc++.h>
using namespace std;

int main(){
   int board,rooks;
   while(scanf("%d %d",&board,&rooks)==2){
        int rookX[rooks],rookY[rooks];
        for(int i=0; i<rooks;i++) scanf("%d %d",&rookX[i],&rookY[i]);
        sort(rookX,rookX+rooks);
        sort(rookY,rookY+rooks);
        printf("%d %d\n",rookX[(rooks-1)/2],rookY[(rooks-1)/2]);
   }
   return 0;
}
```
