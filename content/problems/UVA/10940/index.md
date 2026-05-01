---
title: "10940 — UVA"
summary: "Solución al problema 10940 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 10940

```cpp
#include <bits/stdc++.h>
using namespace std;

int ans [500005];

int main ()
{
    ans [1] = 1; ans [2] = 2;
    int next = 2,n;
    for (int i = 3; i <= 500000; i++ ) {
        if ( i < next ) next = 2;
        ans [i] = next;
        next += 2;
    }
    while ( scanf ("%d", &n)==1 && n!=0) printf ("%d\n", ans [n]);
    return 0;
}
```
