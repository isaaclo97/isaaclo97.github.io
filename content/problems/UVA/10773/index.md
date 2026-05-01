---
title: "10773 — UVA"
summary: "Solución al problema 10773 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 10773

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main() {
    double d,v,u,t1,t2;
    int T,ca=1;
    cin>>T;
    while(T--){
        cin>>d>>v>>u;
        if(v>=u || u==0 || v==0)
            printf("Case %d: can't determine\n",ca++);
        else {
        t1=d/u;
        t2=d/sqrt(u*u-v*v);
        printf("Case %d: %.3lf\n",ca++,fabs(t2-t1));}
    }
    return 0;
}
```
