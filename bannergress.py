import json
import io
import requests

URL = "https://api.bannergress.com:443/bnrs?orderBy=created&orderDirection=DESC&placeId=netherlands-2585&limit=100&offset="

file = open("out.txt","r+")
file.truncate(0)
file.close()

for i in range(0,1000000, 100):
    resp = requests.get(URL + str(i))
    results = resp.json()
    print(results)
    if len(results) == 0:
        exit(0)
    for result in results:
        with io.open("out.txt", 'a', encoding="utf-16") as w:
            title = result['title']
            # print(title)
            city = result['formattedAddress'].split(", Netherlands")[0]
            if city[0].isdigit() and city[1].isdigit() and city[2].isdigit() and city[3].isdigit():
                city = city[4:]
                if len(city) > 3 and city[0].isupper() and city[1].isupper() and city[2] == " ":
                    city = city[3:]
            # print(city)
            size = result['numberOfMissions']
            # print(size)
            rawdistance = result['lengthMeters']
            distance = str(round(rawdistance/1000, 2))
            distance = str(distance).replace(".", ",")
            # print(distance)
            distance_per_image = str(round(rawdistance / 1000 / size, 2))
            distance_per_image = str(distance_per_image).replace(".", ",")
            # print(distance_per_image)
            specopslink = "https://bannergress.com/banner/" + result['id']
            # print(specopslink)
            w.write((title + ";" + city + ";" + str(size) + ";" + str(distance) + ";" + str(distance_per_image) + ";" + specopslink + "\n"))