---
title: "11586 — UVA"
summary: "Solución al problema 11586 de UVA."
tags: ["UVA", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 11586

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int cases,count=0;
    cin>>cases;
    cin.ignore();
    while(cases--)
    {
        count=0;
        string temp;
        getline(cin, temp);
                for (unsigned int i = 0; i< temp.length(); i++)
                {
                    if (temp[i] == 'M')
                        count++;
                    else if (temp[i] == 'F')
                        count--;
                }

                if (count == 0 && temp.length() > 3)
                    cout << "LOOP\n";
                else
                    cout << "NO LOOP\n";
    }
    return 0;
}
```
