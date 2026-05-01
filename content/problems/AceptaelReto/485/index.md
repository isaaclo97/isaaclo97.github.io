---
title: "485 — AceptaelReto"
summary: "Solución al problema 485 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 485

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    while(scanf("%d",&n)==1 && n!=0)
    {
        long long int total = 0;
        int arr[n];
        for(int i=0; i<n;i++)
        {
            scanf("%d",&arr[i]);
            total+=arr[i];
        }
        for(int i=0; i<n;i++)
        {
            if(i==0) printf("%lld",total);
            else printf(" %lld",total);
            total-=arr[i];
        }
        printf("\n");
    }
    return 0;
}
```
