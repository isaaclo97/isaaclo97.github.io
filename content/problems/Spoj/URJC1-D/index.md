---
title: "URJC1_D — Spoj"
summary: "Solución al problema URJC1_D de Spoj."
tags: ["Spoj", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — URJC1_D

```cpp
///Rollitos URJC

#include <iostream>
using namespace std;
int main()
{
    int casos,rollitos,personas;
    cin >> casos;
    while(casos--)
    {
        cin>>personas>>rollitos;
        if(rollitos%personas==0)
        {
            cout << rollitos/personas<<"\n";
        }
        else
            cout << "BRING ME MOAR SUSHI!\n";
    }
    return 0;
}
```
