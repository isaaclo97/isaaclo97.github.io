---
title: "Algoritmo de LCS."
type: page
---

```cpp
/**
* Author: Isaac
* Date: 2009-04-06
* License: -
* Source:
* Description: Longest Common Substring
*/
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
```
