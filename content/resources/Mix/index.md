---
title: "Algoritmo de Mix."
type: page
---

```cpp
PI: 4 * atan(1)
Distancia Euclediana: sqrt(pow(q[i].x-actual.x,2.0)+
pow(q[i].y-actual.y,2.0)+ pow(q[i].z-actual.z,2.0));
Distancia Manhattan: abs(x-x)+abs(y-y)
INF: 0x3F3F3F3F
//number too large. use powl instead of pow.
powl(a, b)
int sx[]={1,-1,0,0,1,-1,-1,1}; //8 directions
int sy[]={0,0,1,-1,1,-1,1,-1};
int sx[]={1,-1,0,0}; //4 directions
int sy[]={0,0,1,-1};
int dx2[]={-2,-1,1,2,2,1,-1,-2}; //horse jumps
int dy2[]={1,2,2,1,-1,-2,-2,-1};
scanf("%d:%d", &hr, &temp, &min);
printf("%02d:%02d\n", hr, min);
(int)round(p, (1.0/n))
printf("%.1f\n", (a * b)/2);
void copy(first, last, result);
void swap(a,b);
void reverse(first, last);
void reverse_copy(first, last, result);
int find(const string &s2, int pos1 = 0);
cout << s1.str() << endl;
bool operator<(const cosa &other)const{ return weight < other.weight; }
pq.push(cosa{numer,2,numer});
char str[90];
gets(str)
sscanf(str, "%d:%d:%d", &hh, &mm, &ss);
//freopen("in.txt","r",stdin);
//freopen("out.txt","r",stdout);
x & -x //is the least bit in x.
x && !(x & (x - 1)) //true, if x is power of 2.
private long getXorFrom1ToX(long x) {
    if (x == 0 || x == 1) return x;
    if (x == 2) return 3;
    if (x == 3) return 0;
    long l = Long.highestOneBit(x);
    if (x % 2 == 1) return getGr(x - l);
    return l + getGr(x - l);
  }
  
 
double DEG_to_RAD(double d) { return d * PI / 180.0; } //RADIANS = LENGTH

double RAD_to_DEG(double r) { return r * 180.0 / PI; }

unsigned int reverse_bits(unsigned int v){
    v = ((v >> 1) & 0x55555555) | ((v & 0x55555555) << 1);
    v = ((v >> 2) & 0x33333333) | ((v & 0x33333333) << 2);
    v = ((v >> 4) & 0x0F0F0F0F) | ((v & 0x0F0F0F0F) << 4);
    v = ((v >> 8) & 0x00FF00FF) | ((v & 0x00FF00FF) << 8);
    return ((v >> 16) | (v << 16));
}

/// Returns i if x = 2^i and 0 otherwise
int bitscan(unsigned int x){
    __asm__ volatile("bsf %0, %0" : "=r" (x) : "0" (x));
    return x;
}

/// Returns next number with same number of 1 bits
unsigned int next_combination(unsigned int x){
    unsigned int y = x & -x;
    x += y;
    unsigned int z = x & -x;
    z -= y;
    z = z >> bitscan(z & -z);
    return x | (z >> 1);
}
```
