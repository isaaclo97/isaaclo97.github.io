---
title: "228 — AceptaelReto"
summary: "Solución al problema 228 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 228

```cpp

#include <bits/stdc++.h>
using namespace std;

string line,res;
int idx;
void solve(int val){
    idx++;
    if(line[idx]==' ') {
        return;
    }
    solve(idx);
    solve(idx);
    //cout<<idx<<" "<<val<<endl;
    res=line[val+1]+res;
}

int main(){
    while(getline(cin,line)){
        idx=-1;
        res="";
        solve(-1);
        cout<<res;
        printf("\n");
    }
    return 0;
}
```
