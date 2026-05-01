---
title: "11942 — UVA"
summary: "Solución al problema 11942 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11942

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int cases;
    cin>>cases;
    cout<<"Lumberjacks:\n";
    while(cases--)
    {
       int a,b,c;
       bool menor = false, sol=true;
       cin>>a>>b;
       if(a<b)
           menor=true;
       if(menor)
       {
           for(int i=0; i<8;i++)
           {// 13=a 25=b 39=b 40=a
               cin>>a;
               if(a<b)
                   sol=false;
               b=a;
           }
       }
       else
       { //78=b 61=a
           for(int i=0; i<8;i++)
           {
               cin>>a;
               if(a>b)
                   sol=false;
               b=a;
           }
       }
       if(sol)
           cout<<"Ordered\n";
       else
           cout<<"Unordered\n";
    }
    return 0;
}
```
