---
title: "Algoritmo de FASTINPUT."
type: page
---

```cpp
#include <bits/stdc++.h>
using namespace std;

//inline int getchar_unlocked() { return getchar(); }
inline void fastInput(int &n){
    char ch;
    int sign = 1;
    while(ch = getchar_unlocked(), isspace(ch)) {

    };
    n = 0;
    if(ch == '-')
        sign = -1;
    else n = ch - '0';
    while(ch = getchar_unlocked(), isdigit(ch))
        n = (n << 3) + (n << 1) + ch - '0';
    n *= sign;
}

int main()
{
    int n; fastInput(n);
    return 0;
}
```
