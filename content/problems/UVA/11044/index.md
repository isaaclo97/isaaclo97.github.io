---
title: "11044 — UVA"
summary: "Solución al problema 11044 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11044

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int tc, w,h;
    cin>>tc;
    while(tc--){
        cin>>w>>h;
        printf("%d\n",(w/3)*(h/3));
    }
    return 0;
}
```
