import time
from time import gmtime, strftime
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

foundMatch = True
print("Has found a match: ", foundMatch)


import requests

url = "https://nlp-translation.p.rapidapi.com/v1/translate"

querystring = {"text":"Hello, world!!","to":"es","from":"en"}

headers = {
    'x-rapidapi-host': "nlp-translation.p.rapidapi.com",
    'x-rapidapi-key': "x"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)






print("comparing both photos...")
time.sleep(1)


a = [1,23,4,5,6,7,8]
b = [9,9,9,9,9999,999999,9999]
print(set(a)&set(b))
a = (set(a)&set(b))
print(a)
print(len(a))

scan1 = [0]*2


#i = 0
#for suggestion in response["suggestions"]:
#    scan1[i] = suggestion
#    ++i





print(scan1)

scan2 = scan1

bereit = input("Weiterfahren? Bitte Ja oder Nein eingeben: ")


if(bereit == "Ja"):
    print("funkt")