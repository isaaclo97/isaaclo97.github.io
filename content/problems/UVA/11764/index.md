---
title: "11764 — UVA"
summary: "Solución al problema 11764 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11764

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int casos,num,valor,salb,sala,valor2,val=1;
    cin>>casos;
            while(casos+1!=val)
            {
                salb=0; sala=0;
                cin>>num;
                cin>>valor;
                for(int i=0; i<num-1;i++)
                {
                    cin>>valor2;
                    if(valor<valor2)
                        sala++;
                    if(valor>valor2)
                        salb++;
                            valor=valor2;
                }
                cout<< "Case "<<val << ": "<<sala << " " <<salb<<"\n";
                val++;
            }
    return 0;
}
```
