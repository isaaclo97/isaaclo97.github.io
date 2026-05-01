---
title: "Algoritmo de BinarySearch."
type: page
---

```cpp
/**
* Author: Isaac
* Date:
* License: -
* Source:
* Description: Binary Search
*/
int binary_search(int *array, int searched, int
arraySize) { int first = 0, middle, last = arraySize -
1;
while (first<=last) { middle = (first + last) / 2;
if (searched == array[middle]) return array[middle];
else {
if (array[middle] > searched) last = middle - 1;
else first = middle + 1;
} } return -1; }
```
