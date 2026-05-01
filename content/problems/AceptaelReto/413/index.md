---
title: "413 — AceptaelReto"
summary: "Solución al problema 413 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 413

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,c;
    cin>>a;
    while(a--)
    {
       cin>>b>>c;
       if((b*c)%2!=0)
       {
           cout<<(b*c)/2+1<<" "<<(b*c)/2<<endl;
       }
       else
            cout<<(b*c)/2<<" "<<(b*c)/2<<endl;

    }
    return 0;
}
```
