import requests
from apiKeys import x_rapidapi_key


def translateFromENtoDE(text):

    url = "https://nlp-translation.p.rapidapi.com/v1/translate"

    querystring = {"text":text,"to":"es","from":"en"}

    headers = {
    'x-rapidapi-host': "nlp-translation.p.rapidapi.com",
    'x-rapidapi-key': "xy"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text
    
print(translateFromENtoDE("My english is good!"))