---
title: "11687 — UVA"
summary: "Solución al problema 11687 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11687

```cpp
#include <bits/stdc++.h>
using namespace std;

string toString(long number){
    stringstream ss;
    ss << number;
    return ss.str();
}
int main() {
    string str ;
    while(cin >> str){
        if( str=="END" ) break ;
        int ans = 1 ;
        while(str != "1" ){
            int len = str.length();
            ans++;
            str = toString(len);
        }
        cout<<ans<<endl;
    }
    return 0;
}
```
