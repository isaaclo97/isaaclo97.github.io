---
title: "11479 — UVA"
summary: "Solución al problema 11479 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11479

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main()
{
    int l,cases=1; cin>>l;
    while(l--)
    {
        long long int first, second, third;
        cin >> first >> second >> third;
        cout << "Case " << cases++ << ": ";
        if (first <= 0 || second <= 0 || third <= 0 ||first + second <= third || first + third <= second || second + third <= first) cout << "Invalid\n";
        else if (first == second && second == third) cout << "Equilateral\n";
        else if (first == second || first == third || second == third) cout << "Isosceles\n";
        else cout << "Scalene\n";
    }
    return 0;
}
```
