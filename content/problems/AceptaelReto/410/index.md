---
title: "410 — AceptaelReto"
summary: "Solución al problema 410 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 410

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    while(n--)
    {
    string str;
    cin>>str;
    bool var [str.length()];
    memset(var,false,sizeof(var));
    int p=0;
    for(unsigned int i=0; i<str.length();i++)
    {
        p+=str[p]-48;
        var[p]=true;
        if(p>=str.length())
        {
           p= p%str.length();
           var[p]=true;
        }
    }
    for(unsigned int i=0; i<str.length();i++)
    {
        if(!var[i])
        {
            p=5;
            break;
        }
    }
    if(p==0)
    {
        cout<<"SALTARINES"<<endl;
    }
    else
        cout<<"NORMALES"<<endl;
    }
    return 0;
}
```
