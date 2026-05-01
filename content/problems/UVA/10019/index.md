---
title: "10019 — UVA"
summary: "Solución al problema 10019 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 10019

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;
int a,b,flag=1;
void tobin(unsigned int n)
{
    if (n/2 != 0) {
        tobin(n/2);
    }
    if(flag==1) { if(n%2==1) a++; }
    else { if(n%2==1) b++; }
}

int main()
{
 int n; cin>>n;
    while(n--)
    {
        int num,f;  cin>>num;
        tobin(num);
        flag=2;
        stringstream sstr;
        sstr << hex << to_string(num);
        sstr >> f;
        tobin(f);
        flag=1;
        cout<<a<<' '<<b<<'\n';
        a=b=0;
    }
 return 0;
}
```
