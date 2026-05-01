---
title: "426 — AceptaelReto"
summary: "Solución al problema 426 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 426

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int in;
    cin>>in;
    while(in!=0)
    {
        int suma=0,dividir=0;
        while(in!=0)
        {
            suma+=in;
            dividir++;
            cin>>in;
        }
        if(suma%dividir==0)
            cout<<"REPARTO JUSTO\n";
        else
            cout<<"IMPOSIBLE\n";
        cin>>in;
    }
    return 0;
}
```
