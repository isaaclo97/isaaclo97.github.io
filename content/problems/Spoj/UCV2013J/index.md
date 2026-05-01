---
title: "UCV2013J — Spoj"
summary: "Solución al problema UCV2013J de Spoj."
tags: ["Spoj", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — UCV2013J

```cpp
#include<bits/stdc++.h>
using namespace std;
int main() {
    int cases;
    while(scanf("%d",&cases)&&cases!=0)
    {
    int total,res=0;
    for(int i=0; i<cases;i++)
    {
        cin>>total;
        if((cases/2)<=i)
        res+=total;
    }
    cout<<res<<endl;
    }
    return 0;
}
```
