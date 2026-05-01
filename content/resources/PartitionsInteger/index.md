---
title: "Algoritmo de PartitionsInteger."
type: page
---

```cpp
//4 = 3 + 1 , 2 + 2 , 2 + 1 + 1 ,1 + 1 +1 + 1

#include <bits/stdc++.h>
using namespace std;
void printAllUniqueParts(int n) {
    int p[n]; int k = 0;  p[k] = n;
    while (true) {
        for(int i=0;i<k+1;i++)
        cout<<p[i]<<" ";
        cout<<endl;
        int rem_val = 0;
        while (k >= 0 && p[k] == 1) {
            rem_val += p[k];
            k--; }
        if (k < 0)  return;
        p[k]--;
        rem_val++;
        while (rem_val > p[k]) {
            p[k+1] = p[k];
            rem_val = rem_val - p[k];
            k++;  }
        p[k+1] = rem_val;
   k++; } }
    int main()
    {
       printAllUniqueParts(4);
       return 0;
    }
```
