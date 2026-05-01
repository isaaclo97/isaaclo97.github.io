---
title: "254 — AceptaelReto"
summary: "Solución al problema 254 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 254

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
 int n;
 cin>>n;
 while(n!=0)
 {
     int arr[n];
     int arr1[n];
     for(int i=0; i<n;i++)
     {
         cin>>arr[i];
     }
     for(int i=0; i<n;i++)
     {
         cin>>arr1[i];
     }
     sort(arr,arr+n);
     sort(arr1,arr1+n);
     int suma=0;
     for(int i=0;i<n;i++)
     {
         suma+= abs(arr[i]-arr1[i]);
     }
     cout<<suma<<endl;
     cin>>n;
 }
    return 0;
}
```
