import requests
import time

f=open("te.txt", "r")
c = f.read()
#c = "Antebellum"
r = []

def checkPsnName(x):
    c = {'onlineId' : x, 'reserveIfAvailable' : False}
    return requests.post("https://accounts.api.playstation.com/api/v1/accounts/onlineIds", json=c)

for w in c.split():
    time.sleep(10)
    p = checkPsnName(w)
    if p.status_code == 200:
        print("Timed out, sleeping one min.. ")
        time.sleep(61)
        p = checkPsnName(w)
        print(w, p, p.ok)
        if p.status_code == 201:
            print("Success!!")
            r.append(w)
    else:
        print(w, p, p.ok)
        if p.status_code == 201:
            print("Success!!")
            r.append(w)

print(len(r), "Available Name(s) Found.")
for n in r:
    print("-", n)
