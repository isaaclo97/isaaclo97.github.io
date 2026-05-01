---
title: "977A — Codeforces"
summary: "Solución al problema 977A de Codeforces."
tags: ["Codeforces", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 977A

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    long long int a,b; cin>>a>>b;
    while(b--)
    {
        if(a%10!=0) a-=1;
        else a/=10;
    }
    cout<<a<<endl;
    return 0;
}
```
