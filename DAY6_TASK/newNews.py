import requests
data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=665d6300777b4adca8bc0062759a527c")
#print(data.text)
items = data
a = [ ]
for i in data:
    i.append(data)
print(a)