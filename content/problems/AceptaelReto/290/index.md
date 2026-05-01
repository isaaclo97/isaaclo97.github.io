---
title: "290 — AceptaelReto"
summary: "Solución al problema 290 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 290

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

int main()
{
    int cases;
    cin>>cases;
    cin.ignore();
    while(cases--)
    {
        int res=0;
        string aux;
        stack<int> pile;
        getline(cin,aux);
        if(aux.length()!=1) //not empty
        {
            //first node
            pile.push(1);
            pile.push(1);
            res++;
            for(unsigned int i=1; i<aux.length();i++)
            {
                if(aux[i]=='*')
                {
                int actual= pile.top();
                res=max(res,actual+1);
                pile.pop();
                pile.push(actual+1);
                pile.push(actual+1);
                }
                else pile.pop();
            }
        }
        cout<<res<<endl;
    }
    return 0;
}
```
