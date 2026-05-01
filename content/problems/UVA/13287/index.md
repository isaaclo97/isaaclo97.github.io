---
title: "13287 — UVA"
summary: "Solución al problema 13287 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 13287

```cpp
//Problema F Swerc 2017 Shattered Cake

#include <bits/stdc++.h>
using namespace std;
int main()
{
    int cases;
    while(scanf("%d",&cases)!=EOF)
    {
        long long int num,a,b,res=0; cin>>num;
        for(int i=0; i<num;i++)
        {
            cin>>a>>b;
            res+=(a*b);
        }
        cout<<res/cases<<endl;
    }
    return 0;
}
```
