---
title: "11150 — UVA"
summary: "Solución al problema 11150 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11150

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main()
{
    int n;
    while(scanf("%d", &n) == 1)
    {
        int sum = n;
        while(n >= 3) {
            sum += n/3;
            n = n/3 + n%3;
        }
        if(n == 2)	sum++;
        printf("%d\n", sum);
    }
    return 0;
}
```
