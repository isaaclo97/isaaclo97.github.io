---
title: "Algoritmo de FloydWarshall."
type: page
---

```cpp
#include<bits/stdc++.h>
using namespace std; //No tiene porque ser simétrica!
#define INF 0x3F3F3F3F
   int dist[4][4] = { {  0, 5  ,INF,10},
                      {INF, 0  ,3  ,INF},
                      {INF, INF,0  ,1},
                      {INF, INF,INF,0}};
void floydWarshall ()
{
    int dist[4][4], i, j, k;
    for (i = 0; i < 4; i++)
        for (j = 0; j < 4; j++)
            dist[i][j] = graph[i][j];
    for (k = 0; k < 4; k++)
        for (i = 0; i < 4; i++)
            for (j = 0; j < 4; j++)
                 dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]);
}
int main()
{
    floydWarshall();
    return 0;
}
```
