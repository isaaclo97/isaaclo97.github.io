---
title: "Algoritmo de Topologicalsort."
type: page
---

```cpp
/**
 * Author: Isaac
 * Date: 2018-11-15
 * License: CC0
 * Description: Linear ordering of its vertices such that for every directed edge u -> v from vertex u to vertex v, u comes before v in the ordering
 * Time: O(E + V)
 * Status:
 */
const int MAXN = 100100;
const int INF = 0x3f3f3f3f;

vector<int> graph[MAXN];
bool visited[MAXN];
stack<int> topological_order;

int N,E;

void DFS(int node){
  if(visited[node]) return;
  visited[node] = true;
  for(int i=0;i<graph[node].size();i++){
    int dest = graph[node][i];
    DFS(dest);
  }
  topological_order.push(node);
}

int main(){
  scanf("%d %d",&N,&E);
  for(int i=1;i<=N;i++) graph[i].clear(); // clean graph
	for(int i=0;i<E;i++){
    int from, to; scanf("%d %d",&from, &to);
    graph[from].push_back(to);
	}
  //Supposing node 1 is not dependent has no ancestor
  DFS(1);
  while(!topological_order.empty()){
    printf(" %d",topological_order.top());
    topological_order.pop();
  }
  printf("\n");
  return 0;
}
```
