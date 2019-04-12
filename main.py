import requests

#f=open("te.txt", "r")
#c = f.read()
c = "noteworthy"

def checkPsnName(x):
    c = {'onlineId' : x, 'reserveIfAvailable' : False}
    return requests.post("https://accounts.api.playstation.com/api/v1/accounts/onlineIds", json=c)

for w in c.split():
    p = checkPsnName(w)
    print(w, p, p.ok)
