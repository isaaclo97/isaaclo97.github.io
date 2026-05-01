---
title: "1A — Codeforces"
summary: "Solución al problema 1A de Codeforces."
tags: ["Codeforces", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 1A

```cpp
#include <iostream>
using namespace std;

int main() {
	long long int a,n,m;
	cin>>n>>m>>a;
	cout<< ((n+a-1)/a)*((m+a-1)/a) <<endl;
	return 0;
}
```
