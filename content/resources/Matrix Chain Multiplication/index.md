---
title: "Algoritmo de Matrix Chain Multiplication."
type: page
---

```cpp
/*
Matrix Chain Multiplication

  0     1     2     3
[2,3] [3,6] [6,4] [4,5]

1 -> (0,1)(2,3) = 2*3*6+6*4*5+2*6*5 = 36 + 120 + 60 = 216
2 -> ((0,1)2))3 = 2*3*6+2*6*4+2*4*5 = 36 + 48 + 40 = 216

     0 | 1 | 2 | 3
 0 | 0   36  84 124
 1 |     0   72 132
 2 |         0  120
 3 |             0

 l = 1 sera siempre 0 porque estamos cogiendo la misma matriz consigo mismo
 l = 2
   (0,1) 2*3*6 = 36
   (1,2) 3*6*4 = 72
   (2,3) 6*4*5 = 120
 l = 3
   (0,1,2) = (0,1)(2,2)
   1. (1,2)+2*3*4 = 96
   2. (0,1)+2*6*4 = 84
   (1,2,3) = (1,2)(3,3)
   1. (2,3)+3*6*5 = 210
   2. (1,2)+3*4*5 = 132
 l = 4
   (0,1,2,3) = (0,1)(2,2)
   1. 0*(1,2,3) = 132+2*3*5 = 162
   2. (0,1)*(2,3) = 32+120+2*6*5=216
   3. (0,1,2)*3 = 84+2*4*5= 124

   T[i][j] = min {T[i][k]+T[k+1][j]+val[i].first*val[k].second*val[j].second}

*/
/*
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
#define n 4
using namespace std;

int arr[] = {1, 2, 3, 4};
int dp[n][n];

int topDown(int i, int j)
{
    if(i==j) return 0;
    if(dp[i][j]!=-1) return dp[i][j];
    dp[i][j]=INF;
    for(int k=i; k<=j;k++)
    {
        int temp = topDown(i,k)+topDown(k+1,j)+arr[i-1]*arr[k]*arr[j];
        dp[i][j]=min(dp[i][j],temp);
    }
    return dp[i][j];
}

int main()
{
    memset(dp,-1,sizeof(dp));
    int m[n][n];

    for (int i=1; i<n; i++) m[i][i] = 0; // cost is zero when multiplying one matrix.

    for (int L=2; L<n; L++) // L is chain length.
        for (int i=1; i<n-L+1; i++)
        {
            int j = i+L-1;
            m[i][j] = INT_MAX;
            for (int k=i; k<=j-1; k++)
            {
                // q = cost/scalar multiplications
                int q = m[i][k] + m[k+1][j] + arr[i-1]*arr[k]*arr[j];
                if (q < m[i][j])  m[i][j] = q;
            }
        }

    cout<<m[1][n-1]<<endl;
    cout<<topDown(1,n-1)<<endl;
    return 0;
}
*/

#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;

long long int dp[105][105];
long long int arr[105];

long long int sum(int j,int e)
{
    long long res=0;
    for(int i=j; i<=e;i++)
    {
        res+=arr[i];
        res%=100;
    }
    return res;
}
long long int solve(int i, int j)
{
    if(i>=j) return 0;
    if(dp[i][j]!=-1) return dp[i][j];
    dp[i][j]=INF;
    for(int k=i; k<=j;k++)
    {
        long long int temp = solve(i,k)+solve(k+1,j);
        temp+=sum(i,k)*sum(k+1,j); //arr[i-1]*arr[k]*arr[j];
        dp[i][j]=min(dp[i][j],temp);
        //dp[i][j] =min(dp[i][j],solve(i,k)+solve(k+1,j)+sum(i,k)*sum(k+1,j));
    }
    return dp[i][j];
}

int main()
{
    freopen("C:/Users/Isaac/Documents/QT/Entregar/in.txt","r",stdin);
    //freopen("C:/Users/Isaac/Documents/QT/Entregar/out.txt","w",stdout);
    int n;
    while(scanf("%d",&n)==1)
    {
    memset(dp,-1,sizeof(dp));
    for(int i=0; i<n;i++) { cin>>arr[i]; color[i][i]=arr[i]; }
    cout<<solve(0,n-1)<<'\n';
    }
    return 0;
}
```
