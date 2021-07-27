import json
import requests
data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=665d6300777b4adca8bc0062759a527c")
print(data.text)

Extractdata = data.json()
print(Extractdata)
articles=Extractdata["articles"]
for i in articles:
    print(i["title"])
