---
title: "Algoritmo de PalindromeString."
type: page
---

```cpp
/**
* Author: Isaac
* Date: 2009-04-06
* License: -
* Source:
* Description: Tower of Hanoi
*/
bool isPalindrome[100][100];

int main()
{
	string s; cin>>s;
	int len=s.size();
	for(int i=0; i<len; i++) isPalindrome[i][i]=true;
	for(int k=1; k<len; k++)
	{
		for(int i=0; i+k<len; i++)
		{
			int j=i+k;

			isPalindrome[i][j]=(s[i]==s[j]) && 
			(isPalindrome[i+1][j-1] || i+1>=j-1);
		}
	}
	return 0;
}
```
