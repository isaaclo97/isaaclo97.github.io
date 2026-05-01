---
title: "1066A — Codeforces"
summary: "Solución al problema 1066A de Codeforces."
tags: ["Codeforces", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 1066A

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int cases,L,l,v,r; cin>>cases;
    while(cases--)
    {
        scanf("%d%d%d%d",&L,&v,&l,&r);
        int res = (l-1)/v;
        res+=(L-r)/v;
        int resto = (L-r)%v;
        int aux = 0;
        if(r%v!=0)  {
            aux=((r/v)+1)*v;
            if(r+resto>=aux) res++;
        }
        printf("%d\n",res);
    }
    return 0;
}
```
