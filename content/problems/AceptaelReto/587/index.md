---
title: "587 — AceptaelReto"
summary: "Solución al problema 587 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 587

```cpp

#include <bits/stdc++.h>
using namespace std;

int main(){
    int cases; scanf("%d",&cases); cin.ignore();
    while(cases--){
        string line; getline(cin,line);
        int res = 0;
        char color;
        for(unsigned int i=0; i<line.length();i++){
            if(i%2==0) {
                color=line[i+1];
                if(color==line[i]) res++;
            }
            else{
                if(color==line[i]) res++;
            }
        }
        printf("%d\n",res);
    }
    return 0;
}
```
