---
title: "272 — AceptaelReto"
summary: "Solución al problema 272 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 272

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;
void convert(int num) {
    if (num>0) {
        convert(num/6);
        cout<<num%6;
    }

}
int main()
{
    int cases;
    cin>>cases;
    while(cases--)
    {
        int num; cin>>num;
        if(num==0) cout<<"0";
        else convert(num);
        cout<<"\n";
    }
}
```
