---
title: "LASTDIG — Spoj"
summary: "Solución al problema LASTDIG de Spoj."
tags: ["Spoj", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — LASTDIG

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ULLI;
typedef unsigned int UI;
 
UI bin_pow(UI a, ULLI n) {
    UI result = 1;
    while (n) {
        if (n & 1) {
            result = (result * a) % 10;
            n -= 1;
        } else {
            a = (a * a) % 10;
            n >>= 1;
        }
    }
    return result;
}
 
int main() {
    int n;
    cin >> n;
    while (n--) {
        string a;
        ULLI b;
        cin >> a >> b;
        cout << bin_pow(a.back() - '0', b) << endl;
    }
}
```
