---
title: "Algoritmo de LongestIncreasingCommonSubsequence."
type: page
---

```cpp
// 2 3 1 6 5 4 6 AND 1 3 5 6 the LCIS is 3 5 6.
#include<iostream>
using namespace std;
int a[100]={0};
int b[100]={0};
int f[100]={0};
int n=0, m=0;
int main(void)
{
cin >> n;
for (int i=1;i<=n;i++) cin >> a[i];
cin >> m;
for (int i=1;i<=m;i++) cin >> b[i];
for (int i=1;i<=n;i++)
{
int k=0;
for (int j=1;j<=m;j++) {
if (a[i]>b[j] && f[j]>k) k=f[j];
else if (a[i]==b[j] && k+1>f[j]) f[j]=k+1;
} }
int ans=0;
for (int i=1;i<=m;i++)
if (f[i]>ans) ans=f[i];
cout << ans << endl;
             return 0;}
```
