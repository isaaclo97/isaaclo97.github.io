---
title: "427 — AceptaelReto"
summary: "Solución al problema 427 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 427

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int cases;
    cin>>cases;
    while(cases--)
    {
        string a, b;
        cin>>a>>b;
        if(a=="Luke"&&b=="padre")
            cout<<"TOP SECRET\n";
        else
            cout<<a<<", yo soy tu "<<b<<endl;
    }
    return 0;
}
```
