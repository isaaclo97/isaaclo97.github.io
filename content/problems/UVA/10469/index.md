---
title: "10469 — UVA"
summary: "Solución al problema 10469 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 10469

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main() {
   unsigned int a,b;
   while(scanf("%d%d",&a,&b)==2)
   {
       printf("%d\n",a^b);
   }
    return 0;
}
```
