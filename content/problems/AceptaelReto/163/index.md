---
title: "163 — AceptaelReto"
summary: "Solución al problema 163 de AceptaelReto."
tags: ["AceptaelReto", "competitive-programming"]
categories: ["Programación Competitiva"]
type: page
---

## Solución — 163

```cpp
import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        String aux = s.nextLine();
        while(!aux.equals("FIN")) {
            BigInteger bigInt = new BigInteger(aux, 16);
            bigInt = bigInt.add(BigInteger.ONE);
            String res = bigInt.toString(16);
            System.out.println(res.toUpperCase());
            aux = s.nextLine();
        }
    }
}
```
