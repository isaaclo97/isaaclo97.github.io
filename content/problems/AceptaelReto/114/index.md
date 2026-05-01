---
title: "114 — AceptaelReto"
summary: "Solución al problema 114 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 114

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n; cin >> n;
        if (n == 0) cout << 1 << endl;
        else if (n == 3) cout << 6 << endl;
        else if (n < 5) cout << n << endl;
        else cout << 0 << endl;
    }

    return 0;
}
```
