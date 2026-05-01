---
title: "272 — UVA"
summary: "Solución al problema 272 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 272

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    string all;
    bool first=true;
    while(getline(cin,all))
    {
        string res;
        for(int i=0; i<all.length();i++)
        {
            if(all[i]==34&&first)
            {
                res+="``";
                first=false;
            }
            else if(all[i]==34&&!first)
            {
                res+="''";
                first=true;
            }
            else
               res+=all[i];
        }
        cout<<res<<endl;
    }
    return 0;
}
```
