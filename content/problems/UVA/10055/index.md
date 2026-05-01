---
title: "10055 — UVA"
summary: "Solución al problema 10055 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 10055

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int A,B;
    while(scanf("%lld%lld",&A,&B)!=EOF)
    {
        if(A > B) cout<< A - B<<endl;
        else cout<<B - A<<endl;
    }
}
```
