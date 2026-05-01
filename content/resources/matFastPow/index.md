---
title: "Algoritmo de matFastPow."
type: page
---

```cpp
/**
* Author: Jakub
* Date: 2009-04-06
* License: -
* Source:
* Description: FastPow of any size (square) matrix given as vector<vector<ll>>, resulting values are modulus mod. Also contains matMul which works with any matrix with dimensions (m,n)(k,j) if n equals k;
*/
typedef vector<ll> vl;
vector<vl> createMat(int s, bool ide){
    //create 0 matrix (false) or identity matrix (true)
    vector<vl> mat(s);
    for(int i=0; i<s;i++){
        for(int j=0;j<s;j++) mat[i].push_back((i==j&&ide)?1:0);}
    return mat;
}
vector<vl> matMul(vector<vl> m1, vector<vl> m2, int mod){
    vector<vl> res = createMat(m2.size(),false);
    for (int i = 0; i < m1.size(); ++i) 
        for (int j = 0; j < m2[0].size(); ++j)
            for (int k = 0; k < m2.size(); ++k) {
                res[i][j]+=m1[i][k]*m2[k][j];
                res[i][j]%=mod;
            }
    return res;
}
vector<vl> matPow(vector<vl> m, int pow, int mod) {
    if (pow == 0) return createMat(m.size(), true);
    if (pow == 1) return m;
    if (pow == 2) return matMul(m,m,mod);
    if (pow%2==0){
        vector<vl> aux = matPow(m,pow/2,mod);
        return matMul(aux,aux,mod);
    } else {
        vector<vl> aux = matPow(m,pow-1,mod);
        return matMul(aux,m,mod);
    }
}
```
