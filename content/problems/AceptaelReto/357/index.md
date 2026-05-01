---
title: "357 — AceptaelReto"
summary: "Solución al problema 357 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 357

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int solve(int n) {
    if (n == 0) return 0;
    return 1 + solve(n / 2);
}

int main()
{
    int n;
    while(scanf("%d",&n)==1)
    {
        printf("%d\n",solve(n));
    }
    return 0;
}
```
