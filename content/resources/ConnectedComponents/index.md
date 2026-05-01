---
title: "Algoritmo de ConnectedComponents."
type: page
---

```cpp
/**
 * Author: Isaac
 * Date: 2018-11-15
 * License: CC0
 * Description: DFS that solves Connected Components
 * Time: O(E + V)
 * Status: Tested on:
 */
const int MAXN = 100100;
const int INF = 0x3f3f3f3f;

vector<int> graph[MAXN];
bool visited[MAXN];

int N,E;

void DFS(int node){
  if(visited[node]) return;
  visited[node] = true;
  for(int i=0;i<graph[node].size();i++){
    int dest = graph[node][i];
    DFS(dest);
  }
}

int main(){
	scanf("%d %d",&N,&E);
  for(int i=1;i<=N;i++) graph[i].clear(); // clean graph
	for(int i=0;i<E;i++){
    int from, to; scanf("%d %d",&from, &to);
    graph[from].push_back(to);
    graph[to].push_back(from); // undirected or not
	}
  memset(visited,0,sizeof(visited));
  int comps = 0;
  for(int i=1;i<=N;i++){
    if(!visited[i]){
      DFS(i);
      comps++;
    }
  }
  printf("%d components\n", comps);
  return 0;
}
```
