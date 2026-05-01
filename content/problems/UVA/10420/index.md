---
title: "10420 — UVA"
summary: "Solución al problema 10420 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 10420

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main()
{
 int n; cin>>n;
 map<string,int> M;
 string str,line;
 while(n--)
 {
     cin>>str; getline(cin,line);
     M[str]++;
 }
 for(auto m:M)
 {
     cout<<m.first<<' '<<m.second<<'\n';
 }
 return 0;
}
```
