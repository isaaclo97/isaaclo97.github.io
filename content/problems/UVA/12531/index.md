---
title: "12531 — UVA"
summary: "Solución al problema 12531 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 12531

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main ()
{
     int  a ;
     while (scanf ("%d",&a) == 1)
          cout<<((a%6==0) ? "Y\n" : "N\n" ) ;
     return 0 ;
}
```
