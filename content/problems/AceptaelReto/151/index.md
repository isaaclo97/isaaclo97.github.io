---
title: "151 — AceptaelReto"
summary: "Solución al problema 151 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 151

```cpp
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int numero;
    cin>>numero;
    while(numero!=0)
    {
        int numero_;
        bool matriz=true;
        for(int i=0; i<numero;i++)
            for(int j=0; j<numero;j++)
            {
                cin>>numero_;
                if(j==i)
                        {
                            if(numero_!=1)
                                matriz=false;
                        }
                else
                    {
                        if(numero_!=0)
                            matriz=false;
                    }
            }
        if(matriz)
            cout<<"SI\n";
        else
            cout<<"NO\n";

        cin>>numero;
    }
    return 0;
}
```
