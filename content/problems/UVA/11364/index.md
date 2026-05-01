---
title: "11364 — UVA"
summary: "Solución al problema 11364 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11364

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int t, n, x;
    cin>>t;
    while(t--) {
        cin>>n;
        int max = 0, min = 99;
        while(n--) {
            scanf("%d", &x);
            if(x > max) max = x;
            if(x < min) min = x;
        }
        printf("%d\n", (max-min)*2);
    }
    return 0;
}
```
