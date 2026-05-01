---
title: "350 — AceptaelReto"
summary: "Solución al problema 350 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 350

```cpp
#include <iostream>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    while (!(a == 0 && b == 0))
    {
        printf("%.1f\n", a * (double) b/2);
        cin >> a >> b;
    }
    return 0;
}
```
