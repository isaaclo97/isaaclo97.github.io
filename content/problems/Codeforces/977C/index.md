---
title: "977C — Codeforces"
summary: "Solución al problema 977C de Codeforces."
tags: ["Codeforces", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 977C

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main() {
    int n,m; cin>>n>>m;
    int a[n+2];
    a[0]=1; a[n+1]=1000000001;
    for (int i=1;i<=n;i++) cin>>a[i];
    sort(a,a+n+2);
    if (a[m]==a[m+1]) cout<<-1; else cout<<a[m];
    return 0;
}
```
