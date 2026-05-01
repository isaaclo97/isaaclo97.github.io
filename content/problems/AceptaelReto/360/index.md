---
title: "360 — AceptaelReto"
summary: "Solución al problema 360 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 360

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int numero;
    cin>>numero;
    while(numero--)
    {
        long long int a,b,x,d,resultado=0;
        cin>>a>>b;
        d=a;
        cin>>x;
        while(x!=-1)
        {
            d-=x;
            if(d<b)
            {
                resultado++;
                d=a;
            }
             cin>>x;
        }
        cout<<resultado<<endl;
    }
    return 0;
}
```
