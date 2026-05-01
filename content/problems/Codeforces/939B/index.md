---
title: "939B — Codeforces"
summary: "Solución al problema 939B de Codeforces."
tags: ["Codeforces", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 939B

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main()
{
    long long int h,b,aux,maxi=0,type=1,out=0;
    cin>>h>>b;
    for(long long int i=0; i<b;i++)
    {
        cin>>aux;
        long long int res = h/aux;
        long long int auxres = res*aux;
        if(maxi<auxres) {type=i+1; maxi=auxres; out=res;}
    }
    cout<<type<<" "<<out<<endl;
    return 0;
}
```
