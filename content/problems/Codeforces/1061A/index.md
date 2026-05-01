---
title: "1061A — Codeforces"
summary: "Solución al problema 1061A de Codeforces."
tags: ["Codeforces", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 1061A

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n,S; scanf("%d%d",&n,&S);
    if(S%n==0) printf("%d",S/n);
    else printf("%d",S/n+1);
    return 0;
}
```
