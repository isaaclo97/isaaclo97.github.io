---
title: "Algoritmo de Geometry_Polygon_Library."
type: page
---

```cpp
#include <bits/stdc++.h>
using namespace std;
#define EPS 1e-9
#define PI acos(-1.0)
typedef long long int ll;
struct point{
    double x,y;
    point(){x=y=0;}
    point(int _x,int _y){x=_x,y=_y;}
    bool operator <(point other) const{
        if (fabs(x-other.x)>EPS)return x<other.x;
        return y<other.y;
    }bool operator ==(point other) const{
        return (fabs(x-other.x)<EPS)&&
        (fabs(y-other.y)<EPS);
    }
    point operator +(point other) const{
        return point(x+other.x,y+other.y);
    }point operator -(point other) const{
        return point(x-other.x,y-other.y);
    }
};
struct vec {
  double x, y;
  vec(double _x, double _y): x(_x), y(_y) {}
};
vec toVec(point a, point b) { // convert 2 points to vec
  return vec(b.x - a.x, b.y - a.y);
}
double cross(vec a, vec b) {
  return a.x * b.y - a.y * b.x;
}
double cross(point o, point a, point b) {
    return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x);
}
// note: to accept collinear points, we have to change the > 0
// returns true if point r is on the left side of line pq
bool ccw(point p, point q, point r) {
  return cross(toVec(p, q), toVec(p, r)) > 0;
}
// returns true if point r is on the same line as the line pq
bool collinear(point p, point q, point r) {
  return fabs(cross(toVec(p, q), toVec(p, r))) < EPS;
}
double dot(vec a, vec b) {
    return (a.x * b.x + a.y * b.y);
}

double norm_sq(vec v) {
    return v.x * v.x + v.y * v.y;
}
vec scale(vec v, double s) {
    return vec(v.x * s, v.y * s);
}

point translate(point p, vec v) { // translate p according to v
    return point(p.x + v.x, p.y + v.y);
}

bool inPolygon(point P, vector < point > poly) {
  int n = poly.size();
  bool in = 0;
  for (int i = 0, j = n - 1; i < n; j = i++) {
    double dx = poly[j].x - poly[i].x;
    double dy = poly[j].y - poly[i].y;
    if ((poly[i].y <= P.y + EPS && P.y < poly[j].y) || (poly[j].y <= P.y + EPS && P.y < poly[i].y))
      if (P.x - EPS < dx * (P.y - poly[i].y) / dy + poly[i].x)
        in ^= 1;
  }
  for (int i = 0; i < n - 1; i++)
    if (collinear(poly[i], poly[i + 1], P)) return false;
  if (collinear(poly[0], poly[n - 1], P)) return false;
  return in;
}
double calc_area(vector<point> Pa) {
  double ans = 0;
  for (int i = 0; i < (int) Pa.size() - 1; i++)
    ans += Pa[i].x * Pa[i + 1].y - Pa[i].y * Pa[i + 1].x;
  return fabs(ans) / 2.0;
}
point centroid(vector <point> g) //center of mass
{
  double cx = 0.0, cy = 0.0;
  for (unsigned int i = 0; i < g.size() - 1; i++) {
    double x1 = g[i].x, y1 = g[i].y;
    double x2 = g[i + 1].x, y2 = g[i + 1].y;
    double f = x1 * y2 - x2 * y1;
    cx += (x1 + x2) * f;
    cy += (y1 + y2) * f;
  }
  double res = calc_area(g); //remove abs
  cx /= 6.0 * res;
  cy /= 6.0 * res;
  return point(cx, cy);
}

bool isConvex(const vector < point > & P) {
  int sz = (int) P.size();
  if (sz <= 3) return false;
  bool isLeft = ccw(P[0], P[1], P[2]);
  for (int i = 1; i < sz - 1; i++)
    if (ccw(P[i], P[i + 1], P[(i + 2) == sz ? 1 : i + 2]) != isLeft)
      return false;
  return true;
}
  vector <point> CH(vector <point> Pa) {
    vector <point> res;
    sort(Pa.begin(), Pa.end());
    int n = Pa.size();
    int m = 0;
    for (int i = 0; i < n; i++) {
      while (m > 1 && cross(res[m - 2], res[m - 1], Pa[i]) <= 0) res.
      pop_back(), m--;
      res.push_back(Pa[i]), m++;
    }
    for (int i = n - 1, t = m + 1; i >= 0; i--) {
      while (m >= t && cross(res[m - 2], res[m - 1], Pa[i]) <= 0) res.
      pop_back(), m--;
      res.push_back(Pa[i]), m++;
    }
    return res;
  }
  double dist(point p1, point p2) {
    return hypot(p1.x - p2.x, p1.y - p2.y);
  }

  double distToLine(point p, point a, point b, point &c) {
      // formula: c = a + u * ab
      vec ap = toVec(a, p), ab = toVec(a, b);
      double u = dot(ap, ab) / norm_sq(ab);
      c = translate(a, scale(ab, u)); // translate a to c
      return dist(p, c);
  }
  double distToLineSegment(point p, point a, point b, point &c) {
      vec ap = toVec(a, p), ab = toVec(a, b);
      double u = dot(ap, ab) / norm_sq(ab);
      if (u < 0.0) {
          c = point(a.x, a.y); // closer to a
          return dist(p, a);
      }
      if (u > 1.0) {
          c = point(b.x, b.y); // closer to b
          return dist(p, b);
      }
      return distToLine(p, a, b, c);
  }

  double polygonDiameter(int n, point pt[]) { //rotater caliper
      if (n <= 2) return 0;
      double ret = 1e+60;
      point aux;
      pt[n]=pt[0];
      //int n =  pt.size()-1; //just end added
      for (int i = 0, j = 0; i <n; i++) {
              while (cross(pt[i], pt[i+1], pt[j+1]) >= cross(pt[i], pt[i+1], pt[j]))
                  j = (j+1)%n;
              double dist = distToLineSegment(pt[j], pt[i], pt[i+1],aux);
              ret = min(ret, dist);
          }
      return ret;
  }
  double perimeter(const vector<point> &Pa) {
    double result = 0.0;
    for (int i = 0; i < (int)Pa.size()-1; i++)
      result += dist(Pa[i], Pa[i+1]);
    return result; }
int main() {

}
```
