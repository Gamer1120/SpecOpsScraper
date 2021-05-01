import requests, json
import io
URL = "https://specops.quest/api/b/search?geo=[\"Netherlands\"]&page="

file = open("out.txt","r+")
file.truncate(0)
file.close()

for i in range(0,56):
    resp = requests.get(URL + str(i))
    json = resp.json()
    results = json['results']
    for result in results:
        with io.open("out.txt", 'a', encoding="utf-16") as w:
            w.write((result['title'] + ";https://specops.quest/banner/" + result['slug'] + "/missions\n"))