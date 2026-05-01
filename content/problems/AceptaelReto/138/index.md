---
title: "138 — AceptaelReto"
summary: "Solución al problema 138 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 138

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long int casos,n;
    cin>>casos;
    while(casos--)
    {
        cin>>n;
        int r = 0;
               while (n >= 5) {
                   r += n / 5;
                   n /= 5;
                   }
               cout<<r<<"\n";
    }
    return 0;
}
```
