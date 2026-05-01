---
title: "Algoritmo de MatrixChainMultiplication."
type: page
---

```cpp
/**
* Author: Isaac
* Date: 2009-04-06
* License: -
* Source:
* Description: Matrix Chain Multiplication Top Down
*/
#define n 4

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
```
