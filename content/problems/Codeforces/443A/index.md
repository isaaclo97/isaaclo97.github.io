---
title: "443A — Codeforces"
summary: "Solución al problema 443A de Codeforces."
tags: ["Codeforces", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 443A

```cpp
/* Visit: https://isaaclo97.github.io/Programacion.html
 * Author: isaaclo97
 * Time: 2019-11-04 00:08:41
**/

#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
using namespace std;

typedef long long ll;

int main() {
    string line; getline(cin,line);
    set<int> S;
    for(unsigned int i=0; i<line.length();i++){
        if(line[i]=='{'||line[i]=='}'||line[i]==' '||line[i]==',') continue;
        S.insert(line[i]);
    }
    printf("%d",S.size());
    return 0;
}
```
