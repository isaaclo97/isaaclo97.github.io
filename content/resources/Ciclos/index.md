---
title: "Algoritmo de Ciclos."
type: page
---

```cpp
#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100100;
const int INF = 0x3f3f3f3f;

vector<int> graph[MAXN];
bool visited[MAXN];

int a=1, b=6;
int N,E,contador;

bool DFS(int node, int parent){
  if(visited[node])
      return false;
  visited[node] = true;
      bool res = true;
  for(unsigned int i=0;i<graph[node].size();i++){
    int dest = graph[node][i];
    if(dest==parent && visited[dest])
        return true;
    if(visited[dest])
        continue;
    res = DFS(dest,node);
  }
  return res;
}

int main(){
  //freopen("recorridos.in","r",stdin);
    scanf("%d %d",&N,&E);
  for(int i=1;i<=N;i++) graph[i].clear(); // limpia el grafo
    for(int i=0;i<E;i++){
    int from, to; scanf("%d %d",&from, &to);
    graph[from].push_back(to);
    graph[to].push_back(from); // borrar linea si es dirigido
    }
  memset(visited,0,sizeof(visited));
  printf("DFS de %d a %d es %d\n",a,b,DFS(a,b));
  return 0;
}
```
