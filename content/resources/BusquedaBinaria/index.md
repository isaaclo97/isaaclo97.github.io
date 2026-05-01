---
title: "Algoritmo de BusquedaBinaria."
type: page
---

```cpp
#include <bits/stdc++.h>
using namespace std;
int binary_search(int *array, int searched, int arraySize)
{   int first = 0, middle, last = arraySize - 1;
    while (first <= last) { middle = (first + last) / 2;
if (searched == array[middle])  return array[middle];
else {
if (array[middle] > searched) last = middle - 1;
else      first = middle + 1;
}    } return -1; }
int main()
{
    int arraySize, searched; cin >> arraySize;
    int array[arraySize]; cin >> searched;
    binary_search(array, searched, arraySize);
return 0; }
```
