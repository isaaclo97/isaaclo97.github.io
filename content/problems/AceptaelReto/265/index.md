---
title: "265 — AceptaelReto"
summary: "Solución al problema 265 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 265

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    string numero,numero1="";
    cin>>numero;
    while(numero[0]-48!=0)
    {
        long long int suma=0;
            suma+=stoi(numero);
        for(int i=0;i<numero.length()-1;i++)
        {
            for(int j=i+1;j<numero.length();j++)
            {
             numero1+=numero[j];
            }
            suma+=stoi(numero1);
            numero1="";
        }
        cout<<suma<<"\n";
        cin>>numero;
    }
    return 0;
}
```
