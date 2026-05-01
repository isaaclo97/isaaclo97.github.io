---
title: "293 — AceptaelReto"
summary: "Solución al problema 293 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 293

```cpp
#include <iostream>
using namespace std;
int main()
{
   long long int numero,resultado=0,escolo;
   int N;
   cin>>N;
   for(int i=0;i<N;i++)
   {
        for(int i=0;i<5;i++)
        {
         cin>>numero;
            if(i==0)
            {
                resultado+=numero*6;
            }
            else if(i==1)
            {
                resultado+=numero*8;
            }
            else if(i==2)
            {
                resultado+=numero*10;
            }
            else if(i==3)
            {
                escolo=numero;
            }
            else
            {
                resultado+=numero*escolo*2;
            }
   }
        cout<<resultado<<"\n";
                resultado=0;
    }
   return 0;
}
```
