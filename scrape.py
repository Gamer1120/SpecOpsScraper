import requests, json
import io
URL = "https://specops.quest/api/b/search?geo=[\"Netherlands\"]&page="

file = open("out.txt","r+")
file.truncate(0)
file.close()

for i in range(1,9999999999999999999999):
    resp = requests.get(URL + str(i))
    json = resp.json()
    results = json['results']
    print(results)
    if len(results) == 0:
        exit(0)
    for result in results:
        with io.open("out.txt", 'a', encoding="utf-16") as w:
            title = result['title']
            # print(title)
            addressHierarchy = result['addressHierarchy']
            i = len(addressHierarchy) - 1
            while i >= 0:
                if (addressHierarchy[i]) is not None:
                    city = addressHierarchy[i]
                    break
                i -= 1
            # print(city)
            size = result['numMissions']
            # print(size)
            rawdistance = result['distance']
            distance = str(round(rawdistance/1000, 2))
            distance = str(distance).replace(".", ",")
            # print(distance)
            distance_per_image = str(round(rawdistance / 1000 / size, 2))
            distance_per_image = str(distance_per_image).replace(".", ",")
            # print(distance_per_image)
            specopslink = "https://specops.quest/banner/" + result['slug'] + "/missions"
            # print(specopslink)
            w.write((title + ";" + city + ";" + str(size) + ";" + str(distance) + ";" + str(distance_per_image) + ";" + specopslink + "\n"))