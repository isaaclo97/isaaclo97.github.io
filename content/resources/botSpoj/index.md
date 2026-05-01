---
title: "Algoritmo de botSpoj."
type: page
---

```cpp
import glob2
from robobrowser import RoboBrowser
from requests import Session

def login(user, password):
    session = Session()
    # session.verify = False  # Skip SSL verification
    browser = RoboBrowser(session=session, parser="lxml")
    browser.open("http://www.spoj.com/login")
    login = browser.get_forms(class_="form-horizontal")[0]
    login["login_user"].value = user
    login["password"].value = password
    browser.submit_form(login)
    return browser

def submit(browser, url, f):
    browser.open(url)
    form = browser.get_form(id="submit_form")
    form["lang"].value = "44"
    form['subm_file'].value = open(f, 'r')
    browser.submit_form(form)
    #print("Enviado problema " + f)
    #print(browser.parsed)

problems = []
files = [file for file in glob2.glob('*.cpp')]
for f in files:
    p = f.split("/")[-1].split("Problema")[-1].split(".")[0]
    problems.append(p)
#print(problems)
browser = login("", "")

for p, f in zip(problems, files):
 submit(browser, "http://www.spoj.com/submit/" + p, f)
```
