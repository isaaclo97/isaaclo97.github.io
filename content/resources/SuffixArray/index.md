---
title: "Algoritmo de SuffixArray."
type: page
---

```cpp
/**
 * Author: ???
 * Source: PDF UPC
 * License: ???
 * Description: string matching
 * Time: $O(P + T)$ where $P$ is the length of the pattern, $T$ is length of the text
 * Status: Tested
 */
typedef pair<int, int> ii;

#define MAX_N 100010 // O(n log n)
char T[MAX_N]; // up to 100K characters
int n; //length of string
int RA[MAX_N], tempRA[MAX_N];
int SA[MAX_N], tempSA[MAX_N];
int c[MAX_N];
char P[MAX_N]; // the pattern string (for string matching)
int m; // the length of pattern string
int Phi[MAX_N];// for computing LCP
int PLCP[MAX_N];
int LCP[MAX_N];
bool cmp(int a, int b) { return strcmp(T + a, T + b) < 0; }

void countingSort(int k) {  // O(n)
  int i, sum, maxi = max(300, n); // up to 255 chars
  memset(c, 0, sizeof c);
  for (i = 0; i < n; i++)
    c[i + k < n ? RA[i + k] : 0]++;
  for (i = sum = 0; i < maxi; i++) {
    int t = c[i]; c[i] = sum; sum += t;
  }
  for (i = 0; i < n; i++) tempSA[c[SA[i]+k < n ? RA[SA[i]+k] : 0]++] = SA[i];
  for (i = 0; i < n; i++) SA[i] = tempSA[i];
}
void constructSA() { // Up to 100000 characters
  int i, k, r;
  for (i = 0; i < n; i++) RA[i] = T[i];
  for (i = 0; i < n; i++) SA[i] = i;
  for (k = 1; k < n; k <<= 1) {
    countingSort(k);
    countingSort(0);
    tempRA[SA[0]] = r = 0;
    for (i = 1; i < n; i++)
      tempRA[SA[i]] =
      (RA[SA[i]] == RA[SA[i-1]] && RA[SA[i]+k] == RA[SA[i-1]+k]) ? r : ++r;
    for (i = 0; i < n; i++)
      RA[i] = tempRA[i];
    if (RA[SA[n-1]] == n-1) break;
} }

void computeLCP() {
  int i, L;
  Phi[SA[0]] = -1;
  for (i = 1; i < n; i++)
    Phi[SA[i]] = SA[i-1];
  for (i = L = 0; i < n; i++) {// LCP in O(n)
    if (Phi[i] == -1) { PLCP[i] = 0; continue; }
    while (T[i + L] == T[Phi[i] + L]) L++;
    PLCP[i] = L;
    L = max(L-1, 0);
  }
  for (i = 0; i < n; i++)
    LCP[i] = PLCP[SA[i]];
}

ii stringMatching() { // O(m log n)
  int lo = 0, hi = n-1, mid = lo;// valid matching = [0..n-1]
  while (lo < hi) {
    mid = (lo + hi) / 2;
    int res = strncmp(T + SA[mid], P, m);
    if (res >= 0) hi = mid;
    else          lo = mid + 1;
  }
  if (strncmp(T + SA[lo], P, m) != 0) return ii(-1, -1); // if not found
  ii ans; ans.first = lo;
  lo = 0; hi = n - 1; mid = lo;
  while (lo < hi) {
    mid = (lo + hi) / 2;
    int res = strncmp(T + SA[mid], P, m);
    if (res > 0) hi = mid; 
    else         lo = mid + 1;
  }
  if (strncmp(T + SA[hi], P, m) != 0) hi--; 
  ans.second = hi;
  return ans;
}
ii LRS() {
  int i, idx = 0, maxLCP = -1;
  for (i = 1; i < n; i++) // O(n)
    if (LCP[i] > maxLCP)
      maxLCP = LCP[i], idx = i;
  return ii(maxLCP, idx);
}
int owner(int idx) { return (idx < n-m-1) ? 1 : 2; }

ii LCS() {
  int i, idx = 0, maxLCP = -1;
  for (i = 1; i < n; i++) // O(n)
    if (owner(SA[i]) != owner(SA[i-1]) && LCP[i] > maxLCP)
      maxLCP = LCP[i], idx = i;
  return ii(maxLCP, idx);
}
int main() {
  printf("Suffix Array:\n");
  strcpy(T, "GATAGACA");
  n = (int)strlen(T);
  T[n++] = '$';
  //if '\n' uncomment T[n-1] = '$'; T[n] = 0;
  constructSA();// O(n log n)
  printf("\nSR of string T = '%s':\n", T);
  printf(" i\tSA[i]\tSuffix\n");
  for (int i = 0; i < n; i++) printf("%2d\t%2d\t%s\n", i, SA[i], T + SA[i]);
  computeLCP();// O(n)
  ii ans = LRS();
  char lrsans[MAX_N];
  strncpy(lrsans, T + SA[ans.second], ans.first);
  printf("\nLongest Repeated Substring O(n)\n");
  printf("\nLRS is '%s' = %d\n\n", lrsans, ans.first);
  printf("\nString matching O(m log n)\n");
  //printf("\nenter string P below,find P in T:\n");
  strcpy(P, "A");
  m = (int)strlen(P);
  //if '\n' uncomment P[m-1] = 0; m--;
  ii pos = stringMatching();
  if (pos.first != -1 && pos.second != -1) {
    printf("%s is found SA[%d..%d] of %s\n", P, pos.first, pos.second, T);
    printf("They are:\n");
    for (int i = pos.first; i <= pos.second; i++)
      printf("  %s\n", T + SA[i]);
  } else printf("%s is not found in %s\n", P, T);
  printf("\nLongest Common Substring O(n)\n");
  printf("\nRemember, T = '%s'\nNow, enter another string P:\n", T);
  // T already has '$' at the back
  strcpy(P, "CATA");
  m = (int)strlen(P);
  // if '\n' is read, uncomment the next line
  //P[m-1] = 0; m--;
  strcat(T, P);
  strcat(T, "#");
  n = (int)strlen(T);
  //Un prefijo de un sufijo es un substring
  constructSA();
  computeLCP();
  printf("\nLongest Common Prefix O(n)\n");
  printf("\nThe LCP information of 'T+P' = '%s':\n", T);
  printf(" i\tSA[i]\tLCP[i]\tOwner\tSuffix\n");
  for (int i = 0; i < n; i++)
    printf("%2d\t%2d\t%2d\t%2d\t%s\n", i, SA[i], LCP[i], owner(SA[i]), T + SA[i]);
  ans = LCS(); 
  char lcsans[MAX_N];
  strncpy(lcsans, T + SA[ans.second], ans.first);
  printf("\nThe LCS is '%s' = %d\n", lcsans, ans.first);
  return 0;
}
```
