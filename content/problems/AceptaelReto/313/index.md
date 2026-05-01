---
title: "313 — AceptaelReto"
summary: "Solución al problema 313 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 313

```cpp
#include <iostream>
using namespace std;
int main()
{
    int casos;
    int principio,fin;
    cin >> casos;
    for(int i=0; i<casos; i++)
    {
        cin >> principio >> fin;
        if((principio>=0&&fin>=0)||(principio>=0&&principio+fin>=0)||(fin>=0&&fin+principio>=0))
        {
            cout<<"SI\n";
        }
        else
            cout <<"NO\n";
    }
    return 0;
}
```
