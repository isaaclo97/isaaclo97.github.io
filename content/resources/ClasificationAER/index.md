---
title: "Algoritmo de ClasificationAER."
type: page
---

```cpp
from robobrowser import RoboBrowser

def getClasification():
    dict = {}
    for i in range(9550):
        browser = RoboBrowser(history=True,parser="html.parser")
        browser.open("https://www.aceptaelreto.com/user/profile.php?id="+str(i+5))
        soup = browser.parsed
        soup.encode("utf-8")
        j = 0
        print(i)
        name = ""
        for i in soup.find_all("p", class_="form-control-static"):
            aux = i.findAll(text=True)
            aux = str(aux)
            aux = aux[2:-2]
            if j==0:
                nick = aux
            elif j==1:
                name = aux
                break
            j+=1
        for i in soup.find_all('p'):
            aux = i.findAll(text=True)
            aux = str(aux)
            #print(aux)
            if aux[2:11] == "Aceptados":
                name = name + " - " + nick
                res = ""
                for i in aux[12:]:
                    if i != " ":
                        res+=i
                    else:
                        break
                #print(name + " "+ str(res))
                dict[name]=int(res)
                break
    ca1 = 0
    HTML = """<!DOCTYPE html>
    <html>
    <head>
    <style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }
    
    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }
    
    tr:nth-child(even) {
        background-color: #dddddd;
    }
    </style>
    </head>
    <body>
    
    <h2>Clasificacion</h2>
    
    <table>"""
    #print("Clasificacion")
    HTML += """
    <tr>
    <th>Puesto</th>
    <th>Nombre y Nick</th>
    <th>Total</th>
    </tr>
    """
    file = open("Clasification.html", "w", encoding='utf8')
    file.write(HTML)
    #print("Puesto\tNombre y Nick\t\t\tTotal")
    for a in sorted(dict, key=dict.get, reverse=True):
        if dict[a] != 0:
            c1 = "<th>"+ str(ca1+1) + "</th>"
            c2 = "<th>"+ a + "</th>"
            c3 = "<th>"+ str(dict[a]) + "</th>"
            HTML = "<tr>"+c1+c2+c3+"</tr>\n"
            file.write(HTML)
            #print(ca1+1,"\t   ",a,':\t ',dict[a])
            ca1+=1
    #print()
    usersAC = "<h2>Usuarios al menos con 1 problema: " + str(ca1) + " de 9500</h2>\n"
    HTML = "</table>\n"+usersAC+"\n</body>\n </html>"
    #print('Usuarios al menos con 1 problema: ',ca1)
    file.write(HTML)

    file.close()
getClasification()
```
