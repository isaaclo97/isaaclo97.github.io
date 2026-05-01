---
title: "10107 — UVA"
summary: "Solución al problema 10107 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 10107

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main()
{
    int n;
    vector<int> v;
        while(cin>>n)
        {
            v.push_back(n);
            sort(v.begin(),v.end());
            if(v.size()%2==1) cout<<v[(v.size()+1)/2-1]<<endl;
            else cout<<(v[(v.size()+1)/2-1]+v[(v.size()+1)/2])/2<<endl;
        }
    return 0;
}
```
