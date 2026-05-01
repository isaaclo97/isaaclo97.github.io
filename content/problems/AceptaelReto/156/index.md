---
title: "156 — AceptaelReto"
summary: "Solución al problema 156 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 156

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int numero,anterior,resultado=0;
    while(cin>>anterior&&anterior>=0)
    {
        resultado=0;
        while(cin>>numero&&numero!=-1)
        {
        resultado+=abs(anterior-numero);
        anterior=numero;
        }
        cout<<resultado<<"\n";
    }
    return 0;
}
```
