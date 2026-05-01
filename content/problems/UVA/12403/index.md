---
title: "12403 — UVA"
summary: "Solución al problema 12403 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 12403

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int cases = 1,number,sum=0;
    cin>>cases;
    string a;
    while(cases--)
    {
       cin>>a;
       if(a=="report")
       cout<<sum<<endl;
       else
       {
       cin>>number;
       sum+=number;
       }
    }
return 0;
}
```
