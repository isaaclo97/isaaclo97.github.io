---
title: "387 — AceptaelReto"
summary: "Solución al problema 387 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 387

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    while(scanf("%d",&n)==1 && n!=0)
    {
        cin.ignore();
        map<char,int> M;
        string num;
        for(int i=0; i<n;i++) {
            cin>>num;
            M[num[num.length()-1]]++;}
        int flag = 0,curmax = 0,sol;
        for(auto m:M){
            if(m.second>curmax) {
                flag=0; curmax=m.second; sol=m.first;
            }
            else if(m.second==curmax) flag=1;
        }
        if(flag==0) printf("%c\n",sol);
        else printf("VARIAS\n");
    }
    return 0;
}
```
