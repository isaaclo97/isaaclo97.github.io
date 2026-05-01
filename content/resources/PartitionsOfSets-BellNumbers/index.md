---
title: "Algoritmo de PartitionsOfSets-BellNumbers."
type: page
---

```cpp
#include<iostream>
using namespace std;
int countP(int n, int k) {
  if (n == 0 || k == 0 || k > n) return 0;
  if (k == 1 || k == n) return 1;
  return  k*countP(n-1, k) + countP(n-1, k-1); }

int main() {
    int a=0;
   for(int i=0; i<5;i++)
//Sin for solo devuelve en X subsets de esa cantidad
   a+=countP(5, i);  a++;
   cout<<a<<endl;  return 0; }
//1,1,2,5,15,52 Bell Numbers
```
