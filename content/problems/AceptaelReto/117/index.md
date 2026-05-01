---
title: "117 — AceptaelReto"
summary: "Solución al problema 117 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 117

```cpp
#include <iostream>
using namespace std;

int main()
{
    int n=0;
    scanf("%d",&n);
    char nombre[n][100];
    string basura;
    for(int i=0; i<n; i++)
    {
        std::cin >> basura >>nombre[i];
        std::cout << "Hola, " << nombre[i] << ".\n";
    }
    return 0;
}
```
