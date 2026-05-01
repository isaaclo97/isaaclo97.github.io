---
title: "434 — AceptaelReto"
summary: "Solución al problema 434 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 434

```cpp
#include<bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin>>n;
    while(n--) {
    int h,m;
    cin>>h>>m;
    if(h>m)
        cout<<"PRINCIPIO\n";
    else
        cout<<"ROMANCE\n";
    }
    return 0;
}
```
