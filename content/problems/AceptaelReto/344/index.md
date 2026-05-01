---
title: "344 — AceptaelReto"
summary: "Solución al problema 344 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 344

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
        int casos;
        cin >> casos;
        while (casos--) {
            int pares,hembra=0,macho=0;
            cin >> pares;
            pares *= 2;
            while (pares--) {
                char a;
                cin >> a;
                if (a == 'H') hembra++;
                else if (a == 'M') macho++;
            }
            if(hembra==macho)
                cout<<"POSIBLE\n";
            else
                cout<<"IMPOSIBLE\n";
        }
    return 0;
}
```
