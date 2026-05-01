---
title: "11909 — UVA"
summary: "Solución al problema 11909 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11909

```cpp
#include <bits/stdc++.h>
#define PI acos(-1.0)
using namespace std;

int main()
{
    double L,W,H,G;
    while(scanf("%lf%lf%lf%lf",&L,&W,&H,&G)==4)
    {
        double volt = L*W*H;
        double d = (L*sin(G*PI/180))/sin((90-G)*PI/180);
        if(G==90) printf("0 mL\n");
        else if(d<=H)
        {
            d = (L*sin(G*PI/180))/sin((90-G)*PI/180);
            double vola = L*d*W/2;
            printf("%.3lf mL\n",volt-vola);
        }
        else if(G){
            d = H*sin((90-G)*PI/180)/sin(G*PI/180);
            double vola = H*d*W/2;
            printf("%.3lf mL\n",vola);
        }
        else{
          printf("%.3lf mL\n",volt);
        }
    }
}
```
