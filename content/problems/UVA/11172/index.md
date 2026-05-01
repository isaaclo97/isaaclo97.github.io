---
title: "11172 — UVA"
summary: "Solución al problema 11172 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11172

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a;
    cin>>a;
    while(a--)
    {
        long long int b,c;
        cin>>b>>c;
        if(b<c)
            cout<<"<"<<endl;
        else if(b>c)
            cout<<">"<<endl;
        else
            cout<<"="<<endl;
    }
    return 0;
}
```
