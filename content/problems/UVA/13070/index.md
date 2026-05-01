---
title: "13070 — UVA"
summary: "Solución al problema 13070 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 13070

```cpp
#include <iostream>
using namespace std;
int main() {
    int casos;
    cin >> casos;
    while (casos--) {
        int nieve, arboles;
        cin >> nieve >> arboles;
        int p[arboles];
        int i = 0, j = 0, l = 0, enpie = 0;

            while (arboles--) {
            cin >> p[j];
            if (p[j] >= nieve && ++enpie > 5)
                while (enpie > 5) {
                    if (p[i] >= nieve)
                        enpie--;
                    i++;
                }
            l = max(l, j-i+1);
            j++;
        }
        cout << l << endl;
    }
    return 0;
}
```
