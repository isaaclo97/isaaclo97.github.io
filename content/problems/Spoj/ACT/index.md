---
title: "ACT — Spoj"
summary: "Solución al problema ACT de Spoj."
tags: ["Spoj", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — ACT

```cpp
#include<bits/stdc++.h>
using namespace std;
int main()
{
int t,n;
string s;
cin>>t;
while(t--)
{
 
cin>>n>>s;
n=s.length()-1;
cout<<s[n]<<endl;
}
return 0;
}
```
