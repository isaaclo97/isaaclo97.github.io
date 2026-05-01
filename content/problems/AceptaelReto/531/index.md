---
title: "531 — AceptaelReto"
summary: "Solución al problema 531 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 531

```cpp

#include <bits/stdc++.h>
using namespace std;

int main(){
    double NR,NRH,NH,NHR,H,R;
    while(scanf("%lf %lf %lf %lf %lf %lf",&NR,&NRH,&NH,&NHR,&H,&R)==6){
        double percentageReplicants = 1-(NRH/NR);
        double percentageHumansAsReplicant = NHR/NH;
        double totalEliminated = percentageReplicants*R + percentageHumansAsReplicant*H;
        if(totalEliminated/10>percentageHumansAsReplicant*H) printf("APRUEBA\n");
        else printf("SUSPENDE\n");
    }
    return 0;
}
```
