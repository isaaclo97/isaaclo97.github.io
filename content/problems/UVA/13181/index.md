---
title: "13181 — UVA"
summary: "Solución al problema 13181 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 13181

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    string linea;
    while(getline(cin,linea))
    {
        int contador=0,resultado=-3;
        bool primero=false;
        for(int i=0; i<linea.length();i++)
        {
                if(linea[i]=='.')
                {
                    contador++;
                    if(i==0)
                    {
                        primero=true;
                    }
                    if(i==linea.length()-1)
                    {
                         resultado=max(resultado,contador-1);
                    }

                }
                else
                {
                    if(primero)
                    {
                        resultado=max(resultado,contador-1);
                        primero=false;
                    }
                     else  if(contador%2==0)
                        {
                            resultado=max(resultado,contador/2-1);
                        }
                        else
                    {
                        if(contador!=1)
                            resultado=max(resultado,(contador+1)/2-1);
                        else
                            resultado=max(resultado,0);
                    }
                    contador=0;
                }
        }
        cout<<resultado<<"\n";
    }
    return 0;
}
```
