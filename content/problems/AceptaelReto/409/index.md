---
title: "409 — AceptaelReto"
summary: "Solución al problema 409 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 409

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int arr[105];
    int cases; scanf("%d",&cases);
    while(cases--)
    {
        int h,n; scanf("%d %d",&h,&n);
        for(int i=0; i<n;i++) scanf("%d",&arr[i]);
        sort(arr,arr+n);
        int res=0;
        if(h<=n)
        {
            h--;
            for(int j=h;j<n;j++)
                if(arr[j]-arr[j-h]<=15){
                    j+=h;
                    res++;
                }
        }
        printf("%d\n",res);
    }
    return 0;
}
```
