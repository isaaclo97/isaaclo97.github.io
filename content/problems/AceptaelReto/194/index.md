---
title: "194 — AceptaelReto"
summary: "Solución al problema 194 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 194

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    int cases; scanf("%d",&cases);
    while(cases--){
        int total=0;
        string line; cin>>line;
        for(unsigned int i=0; i<line.length();i++){
            if(line[i]=='.'){ total++; i+=2; }
        }
        printf("%d\n",total);
    }
    return 0;
}
```
