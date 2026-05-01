---
title: "Algoritmo de BITRange."
type: page
---

```cpp
/**
* Author: Jakub
* Date: 2009-04-06
* License: -
* Source:
* Description: BIT for range updates.
* Usage: Starts at 1
*/
typedef long long ll;
ll B1[100005], B2[100005];
int N=100000; //arraysize

ll query(ll* ft, int b)	{
	ll sum = 0;
	for (; b > 0; b -= (b&-b)) sum += ft[b];
	return sum;
}
void update(ll* ft, int k, ll v) {
	for (; k <= N; k += (k&-k)) ft[k] += v;
}
ll query(int n) { // sum from 1 to n
	return query(B1, n) * n - query(B2, n);
}
ll range_query(int i, int j){ //sum from i to j (both incl)
	return query(j) - query(i - 1);
}
void range_update(int i, int j, ll v){//to update point use i==j
	update(B1, i, v);
	update(B1, j + 1, -v);
	update(B2, i, v * (i - 1));
	update(B2, j + 1, -v * j);
}
```
