---
title: "636 — AceptaelReto"
summary: "Solución al problema 636 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 636

```cpp

#include <bits/stdc++.h>
using namespace std;

int main(){
    int D,N;
    while(scanf("%d %d",&D,&N)==2){
        map<int,int> visited;

        int cnt = 1;
        string res = "0.";
        do{
            visited[D]=cnt;
            cnt++;
            int start = D*10/N;
            D = D*10%N;
            res+=to_string(start);
        }
        while(visited[D]==0 && D != 0);

        if(D==0) cout<<res<<'\n';
        else{
            string newres = "";
            for(int i=0; i<res.length();i++){
                newres += res[i];
                if(visited[D]==i) newres+="|";
            }
            cout<<newres<<"|\n";
        }
    }
    return 0;
}
```
