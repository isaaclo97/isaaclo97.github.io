---
title: "126 — AceptaelReto"
summary: "Solución al problema 126 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 126

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main()
{
    int n,m;
    while(scanf("%d%d",&n,&m)==2 && (n>=0 || m>=0))
    {
        if(n<=m || n==1) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
```
