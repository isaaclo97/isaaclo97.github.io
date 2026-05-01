---
title: "12468 — UVA"
summary: "Solución al problema 12468 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 12468

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int num1,num2,max1,max2,resul;
    while(cin>>num1>>num2,(num1!=-1 || num2!=-1))
    {
        if(num2>=num1)
        {
            max1=num2-num1;
            max2=100-num2+num1;
        }
        else
        {
            max1=num1-num2;
            max2=100-num1+num2;
        }
        resul=min(max1,max2);
        cout<<resul<<"\n";
    }
    return 0;
}
```
