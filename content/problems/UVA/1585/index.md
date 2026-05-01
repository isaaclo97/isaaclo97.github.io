---
title: "1585 — UVA"
summary: "Solución al problema 1585 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 1585

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a;
    cin>>a;
    while(a--)
    {
        int res=0,cont=1;
        string b;
        cin>>b;
        for(int i=0; i<b.length();i++)
        {
            if(b[i]=='O')
            {
                res+=cont;
                cont++;
            }
            else
                cont=1;
        }
        cout<<res<<endl;
    }
    return 0;
}
```
