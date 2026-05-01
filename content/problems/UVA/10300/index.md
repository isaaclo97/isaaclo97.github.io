---
title: "10300 — UVA"
summary: "Solución al problema 10300 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 10300

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int cases,num,a,b,c;
    cin>>cases;
    while(cases--)
    {
        int res=0;
        cin>>num;
        while(num--)
        {
            cin>>a>>b>>c;
            res+=a*c;
        }
        cout<<res<<endl;
    }
return 0;
}
```
