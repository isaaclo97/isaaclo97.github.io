---
title: "919A — Codeforces"
summary: "Solución al problema 919A de Codeforces."
tags: ["Codeforces", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 919A

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main() {
    double a,b,n,c,res=INF;
    cin>>n>>c;
    while(n--)
    {
        cin>>a>>b;
        res=min(res,(c*a)/b);
    }
    printf("%.8lf\n",res);
    return 0;
}
```
