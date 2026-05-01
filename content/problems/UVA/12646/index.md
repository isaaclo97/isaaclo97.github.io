---
title: "12646 — UVA"
summary: "Solución al problema 12646 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 12646

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int A,B,C;
    while(scanf("%d%d%d",&A,&B,&C)==3)
    {
        if(A!=B&&A!=C)
            cout<<"A"<<endl;
        else if(B!=A&&B!=C)
            cout<<"B"<<endl;
        else if(C!=A&&C!=B)
            cout<<"C"<<endl;
        else if(C==A && A==B)
            cout<<"*"<<endl;
    }
    return 0;
}
```
