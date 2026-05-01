---
title: "502 — AceptaelReto"
summary: "Solución al problema 502 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 502

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int cases,n;
    while(scanf("%d",&cases)==1)
    {
     vector<int> v;
     for(int i=0; i<cases;i++)
     {
        scanf("%d",&n);
        vector<int>::iterator upper = upper_bound (v.begin(), v.end(), n);
        if(upper==v.end()) v.push_back(n);
        else *upper=n;
     }
     printf("%d\n",v.size());
    }
    return 0;
}
```
