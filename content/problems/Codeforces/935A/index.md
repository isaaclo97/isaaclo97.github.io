---
title: "935A — Codeforces"
summary: "Solución al problema 935A de Codeforces."
tags: ["Codeforces", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 935A

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;


int main()
{
    long long int num,res=0;
    cin>>num;
    for(int i=1; i<num;i++)
        if(num%i==0)res++;
    cout<<res<<'\n';
}
```
