---
title: "HojasArbolBalanceado"
type: page
---

```cpp
#include <iostream>
using namespace std;
int main() {
int n=1;
long long int sum=0;
while(n!=0) {
        cin >> n;
        int arr[n];
        arr[0]=n;
         if(n!=0) {
             for(int i = 1 ; i <= n ; i++) {
                 cin >> arr[i];
                    if((2 * i) > n)
                        sum += arr[i];
                }
             cout<<sum<<"\n";
             sum=0; }
}
 return 0;
}
```
