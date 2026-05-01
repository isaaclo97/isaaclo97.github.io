---
title: "Algoritmo de NumerosPrimos."
type: page
---

```cpp
//2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,41, 43, 47, 53, 59, 61, 67, 71,
//73, 79, 83, 89, 97
#include <bits/stdc++.h>
using namespace std;

bool prime(int n)
{
if (n<2) return false;
if (n<=3) return true;
if (!(n%2) || !(n%3)) return false;
for (int i=5;i*i<=n;i+=6)
if (!(n%i) || !(n%(i+2))) return false;
return true;
}
int main()
{
    cout<<prime(17);
    return 0;
}
```
