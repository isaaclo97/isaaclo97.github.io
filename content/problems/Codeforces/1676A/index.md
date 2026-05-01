---
title: "1676A — Codeforces"
summary: "Solución al problema 1676A de Codeforces."
tags: ["Codeforces", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 1676A

```cpp

#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int cases; scanf("%d",&cases);
    while(cases--) {
        string n; cin>>n;
        if(n[0]+n[1]+n[2] == n[3]+n[4]+n[5]) cout<<"YES\n";
        else cout<<"NO\n";
    }
    return 0;
}
```
