---
title: "155 — AceptaelReto"
summary: "Solución al problema 155 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 155

```cpp
#include <iostream>
using namespace std;

int main()
{
    int lc=0;
    int la=0;
    do
    {
    cin >> lc;
    cin >> la;
    if(la>=0&&lc>=0)
    printf("%d\n",(la+lc)*2);
    }
    while(!(la<0||lc<0));
        return 0;
}
```
