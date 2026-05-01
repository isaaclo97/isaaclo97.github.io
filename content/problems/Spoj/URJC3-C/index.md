---
title: "URJC3_C — Spoj"
summary: "Solución al problema URJC3_C de Spoj."
tags: ["Spoj", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — URJC3_C

```cpp
//Problema C

 //Triangulos de Pascal
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int m,n,x,temp;
    cin>>m;
    while(m--)
    {
        cin >> temp>>n;
        for(int i=0;i<n;i++)
        {
        x=temp;
            for(int k=0;k<=i;k++)
            {
            cout << x<<" ";
            x = x *(i-k)/(k+1);
            }
        cout << endl;
        }
    }
    return 0;
}
```
