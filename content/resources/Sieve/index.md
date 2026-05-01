---
title: "Algoritmo de Sieve."
type: page
---

```cpp
// Print all primes smaller than or equal to n using Sieve
#include <bits/stdc++.h>
using namespace std;

void Sieve(int n){
    bool prime[n+1];
    memset(prime, true, sizeof(prime));
    for (int p=2; p*p<=n; p++)
        if (prime[p] == true)
            for (int i=p*2; i<=n; i += p) prime[i] = false;

    for (int p=2; p<=n; p++)
       if (prime[p]) cout << p << " ";
}
int main(){
    int n = 30;  Sieve(n);
    return 0;}

	
bitset<100005> bs;
vector<int> primes;

void sieve() {
    bs.set();
    bs[0] = bs[1] = 0;
    for (unsigned int i = 2; i < bs.size(); i++)
        if (bs[i]) {
            for (long long j = (long long) i * i; j < bs.size(); j += i) bs[j] = 0;
            primes.push_back(i);
        }
}
```
