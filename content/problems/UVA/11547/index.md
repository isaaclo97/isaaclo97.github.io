---
title: "11547 — UVA"
summary: "Solución al problema 11547 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11547

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int t, n;
    cin>>t;
    while(t--) {
        cin>>n;
        int x = (n*63+7492)*5-498;
        if(x < 0)
            x *= -1;
        printf("%d\n", x/10%10);
    }
    return 0;
}
```
