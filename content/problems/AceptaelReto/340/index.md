---
title: "340 — AceptaelReto"
summary: "Solución al problema 340 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 340

```cpp
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m,casos;
        cin>>casos;
    while(casos--)
    {
        cin>>n>>m;
        cout<< (n*(2*m+1)+m)<<"\n";
    }
    return 0;
}
```
