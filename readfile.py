import json
dict = []
temp = {}
count = 1


with open('file.txt', encoding='utf8') as f:
    for line in f:
        if (count == 2):
            temp["Genre"] = line
            count = 3
        if (count == 1):
            temp["Name"] = line
            count = 2

        if (count == 3):
            dict.append(temp)
            temp = {}
            count = 1
f.close()

with open("GameSales2017.json", "w") as outfile:
    json.dump(dict, outfile)