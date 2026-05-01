---
title: "13178 — UVA"
summary: "Solución al problema 13178 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 13178

```cpp
#include <iostream>
#include <math.h>
using namespace std;

int main() {
    long long int casos,numero;
    cin>>casos;
    while(casos!=0)
    {
        cin.ignore();
        cin>>numero;
        
        if(numero%3==0||numero%3==2)
            cout<<"SI"<<"\n";
        else
            cout<<"NO"<<"\n";
        casos--;
    }
   
    return 0;
}
```
