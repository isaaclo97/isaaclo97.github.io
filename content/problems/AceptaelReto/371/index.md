---
title: "371 — AceptaelReto"
summary: "Solución al problema 371 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 371

```cpp
#include <iostream>
using namespace std;

int main()
{
    int numero=-1;
    do
    {
    cin >> numero;
    if(numero!=0)
    {
    cout << (3*numero*(numero+1))/2<<"\n";
    }
    }
    while(numero!=0);
    return 0;
}
```
