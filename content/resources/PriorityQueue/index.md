---
title: "Algoritmo de PriorityQueue."
type: page
---

```cpp
#include <bits/stdc++.h>
using namespace std;
struct cosa{
 int weight;
 int modificado;
 int inicial;
 bool operator<(const cosa &other)const{ return weight < other.weight; } };
int main()
{
        priority_queue<cosa> pq;
        for(int i=0;i<5;i++) {
            pq.push(cosa{i,2,i});
        }
        cosa t1 = pq.top();
        pq.pop();
    return 0;
}
```
