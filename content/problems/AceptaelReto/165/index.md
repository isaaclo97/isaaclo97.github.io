---
title: "165 — AceptaelReto"
summary: "Solución al problema 165 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 165

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    string a;
    bool comprobar =true;
    cin>>a;
    while(a[0]!='-')
    {
        int i=a.length();
               while (i--)
               {
                   if(!((a[i]-48)%2==0))
                   {
                       comprobar=false;
                       break;
                   }
               }
        if (comprobar)  cout<<"SI\n";
        else            cout<<"NO\n";
        comprobar=true;
        cin>>a;
    }
    return 0;
}
```
