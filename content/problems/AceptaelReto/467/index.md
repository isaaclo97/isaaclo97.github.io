---
title: "467 — AceptaelReto"
summary: "Solución al problema 467 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 467

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int cases; cin>>cases;
    while(cases--)
    {
        string X,a,Y; cin>>X>>a>>Y;
        string Xaux,Yaux;
        for(unsigned int i=0; i<X.length();i++) Xaux+=tolower(X[i]);
        for(unsigned int i=0; i<Y.length();i++) Yaux+=tolower(Y[i]);
        if(Xaux==Yaux) cout<<"TAUTOLOGIA\n";
        else cout<<"NO TAUTOLOGIA\n";
    }
    return 0;
}
```
