# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=xowww&logNo=220987549179
# https://pjw48.net/wordpress/2017/03/22/make-json-py/
# https://pjw48.net/wordpress/2017/03/23/json-parsing-py/

import json

savedJsonPath = "resources/saveData.json"

saveData = {}

saveData["https://ruliweb.com"] = {}
saveData["https://ruliweb.com"]["connectStatus"] = True
saveData["https://ruliweb.com"]["mails"] = ["createzone@gmail.com", "ireieri@me.com"]

saveData["https://jidae.com"] = {}
saveData["https://jidae.com"]["connectStatus"] = True
saveData["https://jidae.com"]["mails"] = ["createzone@gmail.com"]

# # Print JSON
# print(json.dumps(saveData, ensure_ascii=False, indent="\t"))

# Write JSON
with open(savedJsonPath, 'w', encoding="utf-8") as make_file:
    json.dump(saveData, make_file, ensure_ascii=False, indent="\t")

# Open JSON
with open(savedJsonPath, encoding="utf-8") as data_file:    
    # data = json.load(data_file, object_pairs_hook=OrderedDict)
    data = json.load(data_file)

print(data)
print(data.keys())
print(list(data.keys()))
# print(list(data.keys())[0])
# print(list(data.keys())[1])

for key in data.keys():
    print(key)

# print(data["https://jidae.com"])
# print(data["https://jidae.com"]["connectStatus"])
# data["https://jidae.com"]["connectStatus"] = False
# print(data["https://jidae.com"])
# print(data["https://jidae.com"]["connectStatus"])
# print(data["https://jidae.com"]["mails"])
# print(data["https://ruliweb.com"]["mails"][0])
# print(data["https://ruliweb.com"]["mails"][1])