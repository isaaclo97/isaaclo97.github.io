---
title: "140 — AceptaelReto"
summary: "Solución al problema 140 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 140

```cpp
#include <iostream>
using namespace std;
int main()
{
    int resultado=0;
    string numero;
    while(1)
    {
    cin>>numero;
    if(numero[0]>47)
    {
    for(int i=0;i<numero.length();i++)
    {
        resultado+=numero[i]-48;
        if(i!=numero.length()-1)
        cout<<numero[i]<<" + ";
        else
            cout<<numero[i]<<" ";
    }
    cout<<"= "<<resultado<<"\n";
    resultado=0;
    }
    else
    break;
    }
   return 0;
}
```
