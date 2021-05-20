import requests
import os
import random
import string

symboles = string.ascii_letters + string.digits + "!@#$%^&*()_-+"
random.seed = (os.urandom(1024))

url = "https://servicemicrosoft5.wixsite.com/my-site-2"

villes = open("villes.txt", "r")
allText1 = villes.read()
ville = list(map(str, allText1.split()))

names = open("names.txt", "r")
allText2 = names.read()
name = list(map(str, allText2.split()))

for i in name:
    name_extra = "".join(random.choice(string.digits))

    email = i.lower() + name_extra + "@hotmail.com"

    password = "".join(random.choice(symboles) for i in range(8))

    villeR = random.choice(ville)

    requests.post(url, allow_redirects=False, data={
        "comp-kk8chq09": email,
        "comp-kk8chq04": password,
        "comp-kk8chq0e": villeR
    })
    print("On balance la sauce! email {} password {} ville {}".format(email, password, villeR))
