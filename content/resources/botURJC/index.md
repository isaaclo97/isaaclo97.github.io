---
title: "Algoritmo de botURJC."
type: page
---

```cpp
from robobrowser import RoboBrowser

def getresources():
    browser = RoboBrowser()
    browser.open("http://programming-urjc.herokuapp.com/")
    soup = browser.parsed
    n = 6
    Matrix = [[0 for x in range(n)] for y in range(120)]
    dict = {}
    i1 = 0
    j = 0
    total = 40
    countACs = 1
    aux = 0
    name = ""
    for i in soup.find_all('td'):
        Matrix[i1][j] = i.findAll(text=True)
        if i1 != 0 and j == 0:
            for m in str(Matrix[i1][j]):
                if m != '[' and m != '\'' and m !=']':
                    name+=m

        if i1 != 0 and j!=0 and j!=n-1:
            st = ""
            sta = str(Matrix[i1][j])
            for p in sta:
                if p==' ':
                    break
                if p!='[' and  p!='\'':
                    st+=p
            aux+= int(st)

        j+=1
        if j==n:
            if i1!=0:
                dict[name]=aux
            name=""
            countACs += aux
            Matrix[i1][j-1] = str(aux)
            aux=0
            #print(Matrix[i1])
            i1+=1
            j=0
    print('Problemas totales: ',total)
    print('Total ACs: ',str(countACs),'/',total*i1)
    print('Usuarios totales: ',i1)
    print()
    print('Ranking de usuarios ')
    ca1 = 0
    for a in sorted(dict, key=dict.get, reverse=True):
        if dict[a] != 0:
            print(ca1+1,'',a,': ',dict[a])
            ca1+=1
    print()
    print('Usuarios al menos con 1 problema: ',ca1)

def getweeks(s,problems):
    browser = RoboBrowser()
    link = "http://programming-urjc.herokuapp.com/"
    link+=s
    browser.open(link)
    soup = browser.parsed
    n = problems
    Matrix = [[0 for x in range(n)] for y in range(120)]
    MatrixProblems = [0 for x in range(n)]
    MatrixProblemsACs = [0]*n
    MatrixProblemsTRIEDs = [0]*n
    i1 = 0
    j = 0
    countACs = 0
    name = ""
    for i in soup.find_all('td'):
        Matrix[i1][j] = i.findAll(text=True)

        if i1 == 0 and j!=0:
            for m in str(Matrix[i1][j]):
                if m != '[' and m != '\'' and m !=']' and m!=',':
                    name+=m
            MatrixProblems[j]=name
            name=""
        if i1 != 0 and j!=0 and j!=n:
            st = ""
            sta = str(Matrix[i1][j])
            if sta == '[\'AC\']':
                MatrixProblemsACs[j]+=1
                countACs+=1
            elif sta == '[\'TRIED\']':
                MatrixProblemsTRIEDs[j]+=1
        j+=1
        if j==n:
            name=""
            #print(countACs)
            #print(Matrix[i1])
            i1+=1
            j=0
    for i in range(1,n-1):
        print(MatrixProblems[i],': ',MatrixProblemsACs[i],' ACs\t',MatrixProblemsTRIEDs[i],' Trieds')
    print('Total de ACs: ', countACs,'/',(n-1)*i1)

getresources()
getweeks("SEMANA%201/",12)
getweeks("SEMANA%202-1/",11)
getweeks("SEMANA%202-2/",11)
getweeks("SEMANA%203/",11)
```
