---
title: "Algoritmo de LIS."
type: page
---

```cpp
//Dada una lista de numberos de longitud n, extrae a que es
//la mayor subsecuencia de aumento O(nlogn)
//   INPUT: a vector of integers // Posible solucion
//X= 0, 8, 4, 12, 2, 10, 6 || LCS= 0,8,12
//OUTPUT: a vector containing the longest increasing subsequence

#include <bits/stdc++.h>
using namespace std;
int Ceil(vector<int> &v, int l, int r, int key) {
while (r-l > 1) { int m = l + (r-l)/2;
if (v[m] >= key) r = m;
else l = m; } return r; }
int LIS(vector<int> &v) {
if (v.size() == 0)   return 0;
vector<int> tail(v.size(), 0);
int length = 1;
tail[0] = v[0];
for (size_t i = 1; i < v.size(); i++) {
if (v[i] < tail[0]) tail[0] = v[i];
else if (v[i] > tail[length-1])tail[length++]=v[i];
else tail[Ceil(tail, -1, length-1, v[i])] = v[i];
  } return length;}
```
