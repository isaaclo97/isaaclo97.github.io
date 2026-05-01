---
title: "506 — AceptaelReto"
summary: "Solución al problema 506 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 506

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int cases; scanf("%d",&cases);
    for(int i=0; i<cases;i++)
    {
       int n,m; scanf("%d / %d",&n,&m);
       if(n>=m) printf("BIEN\n");
       else printf("MAL\n");
    }
    return 0;
}
```
