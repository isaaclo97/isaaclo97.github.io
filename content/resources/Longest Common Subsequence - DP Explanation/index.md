---
title: "Algoritmo de Longest Common Subsequence - DP Explanation."
type: page
---

```cpp
/*
Longest Common Subsequence
Input
abcdaf
acbcf
Output
abcf

        | a |  b  |  c  |  d  | a  |  f  |
   |  0   0    0     0     0    0     0
 a |  0   1    1     1     1    1     1
 c |  0   1    1     2     2    2     2
 b |  0   1    2     2     2    2     2
 c |  0   1    2     3     3    3     3
 f |  0   1    2     3     3    3     4


 Primero es todo ceros porque todas ellas con ningun string es 0
 Si tenemos a y a la maxima longitud de la subsecuencia comun mas larga es 1
 En la segunda fila la longitud sera lo maximo de la de arriba o de la izquierda
 siempre y cuando no sean los mismos, si es la misma es la diagonal mas uno

 La solucion sera 4.

 Para saber cual es la longitud, podemos ver de donde viene el 4, como no tiene el
 mismo numero que arriba o izquierda sabemos que f se aade y viene de diagonal.
 Cada vez que tengamos una diagonal se aade ese caracter a la solucion, mientras tanto
 se sigue moviendo hacia la izquierda o arriba.
*/
/*
#include <bits/stdc++.h>
using namespace std;
int lcs(string str1,string str2,int len1, int len2){
    if(len1 == (int)str1.length() || len2 == (int)str2.length()) return 0;
    if(str1[len1] == str2[len2]) return 1 + lcs(str1,str2,len1+1,len2+1);
    else  return max(lcs(str1,str2,len1+1,len2),lcs(str1,str2,len1,len2+1));
}
int main()
{
    string input1 = "acbcf";
    string input2 = "abcdaf";
    cout<<"TOP DOWN: " <<lcs(input1,input2,0,0)<<'\n';

    int T[input1.length()+1][input2.length()+1];
    for(unsigned int i=0; i<=input1.length();i++) T[i][0]=0;
    for(unsigned int i=0; i<=input2.length();i++) T[0][i]=0;

    for(unsigned int i=1; i <= input1.length(); i++)
    {
       for(unsigned int j=1; j <= input2.length(); j++)
       {
           if(input1[i-1]==input2[j-1]) T[i][j]=T[i-1][j-1]+1;
           else T[i][j]=max(T[i-1][j],T[i][j-1]);
           cout<<T[i][j]<<' ';
       }
       cout<<'\n';
    }
    cout<<T[input1.length()][input2.length()]<<'\n';

    cout<<"GET STRING\n";
    string sol;
    int i = input1.length();
    int j = input2.length();
    while(i!=0 && j!=0)
    {
           if(max(T[i-1][j],T[i][j-1])!=T[i][j]) { sol=input2[j-1]+sol; i--; j--;}
           else if(T[i][j-1]==0) i--; else j--;
    }
    cout<<sol<<'\n';
}
*/

//10450 UVA
/*
#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("C:/Users/Isaac/Documents/QT/Entregar/in.txt","r",stdin);
    freopen("C:/Users/Isaac/Documents/QT/Entregar/out.txt","w",stdout);

    string input1;
    while(getline(cin,input1))
    {

    string input2; getline(cin,input2);
    int T[input1.length()+1][input2.length()+1];
    for(unsigned int i=0; i<=input1.length();i++) T[i][0]=0;
    for(unsigned int i=0; i<=input2.length();i++) T[0][i]=0;

    for(unsigned int i=1; i <= input1.length(); i++)
    {
       for(unsigned int j=1; j <= input2.length(); j++)
       {
           if(input1[i-1]==input2[j-1]) T[i][j]=T[i-1][j-1]+1;
           else T[i][j]=max(T[i-1][j],T[i][j-1]);
       }
    }
    cout<<T[input1.length()][input2.length()]<<'\n';
    }
    return 0;

}
*/



/*

        | l |  v  |  x  |  x  | l  |  v  |
   |  0   0    0     0     0    0     0
 x |  0   0    0     1     1    1     1
 x |  0   0    0     1     2    2     2
 l |  0   1    1     1     2    3     3
 v |  0   1    2     2     2    3     4
 l |  0   1    2     2     2    3     4
 v |  0   1    2     2     2    3     4

 n = 2
        | l |  v  |  x  |  x  | l  |  v  |
   |  0   0    0     0     0    0     0
 x |  0   0    0     0     0    0     0
 x |  0   0    0     0     2    2     2
 l |  0   0    0     0     2    3     3
 v |  0   0    2     2     2    3     4
 l |  0   0    2     2     2    3     4
 v |  0   0    2     2     2    3     4

 A number in diagonal it is included

*/

/*
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string input1;
    string input2;
    int n;
    while(scanf("%d",&n)==1 &&  n!=0)
    {
    cin>>input1; cin>>input2;
    int T[input1.length()+1][input2.length()+1];
    memset(T,0,sizeof(T));

    for (int i = 1; i <= input1.length(); i++)
     for (int j = 1; j <= input2.length(); j++) {
         int c = 1;
         while (i-c >= 0 && j - c >= 0 && input1[i-c] == input2[j-c]) {
         if (c >= n)  T[i][j] = max(T[i][j], c + T[i-c][j-c]);
         c++;
        }
        T[i][j] = max(T[i][j], max(T[i-1][j], T[i][j-1]));
        }
    cout<<T[input1.length()][input2.length()]<<'\n';
    }
    return 0;

}
*/
```
