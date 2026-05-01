---
title: "Algoritmo de StableMarriageProblem."
type: page
---

```cpp
/**
* Author: Isaac
* Date: 2009-04-06
* License: -
* Source:
* Description: Stable Marriage Problem
* Time: O(n^2)
*/
// Gale-Shapley algorithm for the stable marriage problem.
// madj[i][j] is the jth highest ranked woman for man i.
// fpref[i][j] is the rank woman i assigns to man j.
// Returns a pair of vectors (mpart, fpart), where mpart[i] gives 
// the partner of man i, and fpart is analogous
/*
The Stable Marriage Problem states that given N men and N women, where each person has ranked all members of the opposite sex in order of preference, 
marry the men and women together such that there are no two people of opposite sex who would both rather have each other than their current partners. 
If there are no such people, all the marriages are "stable".

Consider the following example.

Let there be two men m1 and m2 and two women w1 and w2.
Let m1`s list of preferences be {w1, w2}
Let m2`s list of preferences be {w1, w2}
Let w1`s list of preferences be {m1, m2}
Let w2`s list of preferences be {m1, m2}

The matching { {m1, w2}, {w1, m2} } is not stable because m1 and w1 would prefer each other over their assigned partners. 
The matching {m1, w1} and {m2, w2} is stable because there are no two people of opposite sex that would prefer each other over their assigned partners.

It is always possible to form stable marriages from lists of preferences 
The idea is to iterate through all free men while there is any free man available. Every free man goes to all women in his preference list according 
to the order. For every woman he goes to, he checks if the woman is free, if yes, they both become engaged. If the woman is not free, then the woman 
chooses either says no to him or dumps her current engagement according to her preference list. So an engagement done once can be broken if a woman 
gets better option.
*/
pair<vector<int>, vector<int> > stable_marriage(vector<vector<int> >& madj, vector<vector<int> >& fpref) {
	int n = madj.size();
	vector<int> mpart(n, -1), fpart(n, -1);
	vector<int> midx(n);
	queue<int> mfree;
	for (int i = 0; i < n; i++) {
		mfree.push(i);
	}
	while (!mfree.empty()) {
		int m = mfree.front(); mfree.pop();
		int f = madj[m][midx[m]++];
		if (fpart[f] == -1) {
			mpart[m] = f; fpart[f] = m;
		} else if (fpref[f][m] < fpref[f][fpart[f]]) {
			mpart[fpart[f]] = -1; mfree.push(fpart[f]);
			mpart[m] = f; fpart[f] = m;
		} else {
			mfree.push(m);
		}
	}
	return make_pair(mpart, fpart);
}
```
