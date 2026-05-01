---
title: "11192 — UVA"
summary: "Solución al problema 11192 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11192

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;
void re(string s)
{
    for(int i=s.length()-1; i>=0;i--) cout<<s[i];
}
int main()
{
    int cases;
    while(scanf("%d",&cases)==1 && cases!=0)
    {
        string s,aux="";
        cin>>s;
        cases = s.length()/cases;
        for(unsigned int i=0; i<s.length();i++)
        {
            if(i%cases==0) { re(aux);aux="";}
            aux+=s[i];
        }
        re(aux);
        cout<<endl;
    }
    return 0;
}
```
