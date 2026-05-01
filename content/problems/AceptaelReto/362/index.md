---
title: "362 — AceptaelReto"
summary: "Solución al problema 362 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 362

```cpp
#include <iostream>

using namespace std;
int main()
{
    int casos,numero,mes;
    cin >> casos;
    for(int i=0; i<casos; i++)
    {
        cin>> numero>>mes;
        if(numero == 25 && mes== 12)
        {
            cout << "SI\n";
        }
        else
            cout << "NO\n";

    }
    return 0;
}
```
