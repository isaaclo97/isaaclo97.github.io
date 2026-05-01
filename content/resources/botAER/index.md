---
title: "Algoritmo de botAER."
type: page
---

```cpp
import glob2
from robobrowser import RoboBrowser
from requests import Session
import sys
sys.stdout = open('web.html', 'w')
def login(user, password):
    session = Session()
    # session.verify = False  # Skip SSL verification
    browser = RoboBrowser(session=session, parser="lxml")
    browser.open("https://www.aceptaelreto.com/")
    login = browser.get_forms(class_="navbarForm")[1]
    login["loginForm_username"].value = user
    login["loginForm_password"].value = password
    browser.submit_form(login)
    return browser


def submit(browser, url, f):
    browser.open(url)
    form = browser.get_form(id="sendForm")
    form["language"].value = "CPP"
    form['inputFile'].value = open(f, 'r')
    browser.submit_form(form)
    #print("Enviado problema " + f)
    print(browser.parsed)

problems = []
files = [file for file in glob2.glob('*.cpp')]
for f in files:
    p = f.split("/")[-1].split("Problema")[-1].split(".")[0]
    problems.append(p)

browser = login("", "")

for p, f in zip(problems, files):
 submit(browser, "https://www.aceptaelreto.com/problem/send.php?id=" + p, f)
```
