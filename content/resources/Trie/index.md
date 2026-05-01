---
title: "Algoritmo de Trie."
type: page
---

```cpp
#include <bits/stdc++.h>
#define INF 0x3F3F3F3F
using namespace std;
const int put = 26; //alphabet size
struct TrieNode
{
    struct TrieNode *children[put];
    //bool isEndOfWord; check end of word
    int num;
};

struct TrieNode *getNode(void)
{
    struct TrieNode *pNode =  new TrieNode;
    //pNode->isEndOfWord = false;
    pNode->num=0;
    for (int i = 0; i < put; i++)  pNode->children[i] = NULL;
    return pNode;
}
void insert(struct TrieNode *root, string key)
{
    struct TrieNode *pCrawl = root;

    for (unsigned int i = 0; i < key.length(); i++)
    {
        int index = key[i] - 'a';
        if (!pCrawl->children[index]) pCrawl->children[index] = getNode();
        pCrawl->num++; //add to get repetitions
        pCrawl = pCrawl->children[index];
    }
    pCrawl->num++;
    //pCrawl->isEndOfWord = true;
}
int searchWord(char key,int a)
{
   int index = key - '0';
   if (!auxNode->children[index]) return -1;
   auxNode = auxNode->children[index];
   if(auxNode->isEndOfWord) auxNode->num++;
   if (a==1) auxNode2=auxNode;
   return 0;
} //Check if the word exist. Move with pointers
  //DONT FORGET RESTORE DE POINTER TO THE BEGIN
int search(struct TrieNode *root, string key)
{
    struct TrieNode *pCrawl = root;
    for (unsigned int i = 0; i < key.length(); i++)
    {
        int index = key[i] - 'a';
        if (!pCrawl->children[index]) return 0;
        pCrawl = pCrawl->children[index];
    }
    return pCrawl->num;
}

int main()
{
    int n,m;
    while(scanf("%d%d",&n,&m)==2)
    {
    string word;
    struct TrieNode *root = getNode();
    for(int i=0; i<n;i++) {cin>>word; insert(root,word);}
    for(int i=0; i<m;i++) {cin>>word; cout<<search(root,word)<<'\n';}
    }
    return 0;
}
```
