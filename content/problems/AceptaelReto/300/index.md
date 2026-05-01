---
title: "300 — AceptaelReto"
summary: "Solución al problema 300 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 300

```cpp
#include <iostream>
 using namespace std;
int main()
{
    int casos;
    string palabra;
    bool a=false,e=false,i2=false,o=false,u=false;
    cin >> casos;
    for(int i=0; i<casos; i++)
    {
        cin >> palabra;
        for(int p=0; p< palabra.length();p++)
        {
        if(palabra[p]=='a')
           a = true;
        if(palabra[p]=='e')
           e = true;
        if(palabra[p]=='i')
           i2 = true;
        if(palabra[p]=='o')
           o = true;
        if(palabra[p]=='u')
           u = true;
        }
        if(a&&e&&i2&&o&&u)
        {
            cout << "SI\n";
        }
        else
            cout <<"NO\n";

        a= false; e=false; i2=false; o=false; u=false;
    }
        return 0;
}
```
