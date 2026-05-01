---
title: "Algoritmo de hanoi."
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
void hanoi(int n) 
{
    moveTower(n, 'A', 'B', 'C');
}

void moveTower(int ht, char f, char t, char i)
{
    if (ht > 0)
    {
        moveTower(ht - 1, f, i, t);
        moveRing(ht, f, t);
        moveTower(ht - 1, i, t, f);
    }
}

void moveRing(int d, char f, char t)
{
    cout << "Move ring " << d << " from ";
    cout << f << " to " << t << endl;
}
int main()
{
    cout << "How many disks? ";
    int x; cin >> x;
    hanoi(x);
    return 0;
}
```
