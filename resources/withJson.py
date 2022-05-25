# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=xowww&logNo=220987549179
# https://pjw48.net/wordpress/2017/03/22/make-json-py/
# https://pjw48.net/wordpress/2017/03/23/json-parsing-py/

import sys
import os
import json

# def resource_path(filename):
#     if hasattr(sys, '_MEIPASS'):
#         return os.path.join(sys._MEIPASS, filename)
#     return os.path.join(os.path.abspath("."), filename)

# with open(resource_path('resources/saveData.json'), 'r') as f:
#     print(f.read())

resourcesPath = os.path.abspath("resources")
saveJsonPath = f'{resourcesPath}/saveData.json'
print(f"saveJsonPath : {saveJsonPath}")

saveData = {}

# 세이브 데이터 구조체 Start
saveData["https://ruliweb.com"] = {}
saveData["https://ruliweb.com"]["connectStatus"] = True
saveData["https://ruliweb.com"]["mails"] = ["createzone@gmail.com", "ireieri@me.com"]

saveData["https://jidae.com"] = {}
saveData["https://jidae.com"]["connectStatus"] = True
saveData["https://jidae.com"]["mails"] = ["createzone@gmail.com"]
# 세이브 데이터 구조체 End

# Write JSON
def writeSaveData():
    with open(saveJsonPath, 'w', encoding="utf-8") as make_file:
        json.dump(saveData, make_file, ensure_ascii=False, indent="\t")

# Open JSON
def openSaveData():
    with open(saveJsonPath, encoding="utf-8") as data_file:    
        savedData = json.load(data_file)

    return savedData

# # Print JSON
# print(json.dumps(saveData, ensure_ascii=False, indent="\t"))

# data = openSaveData()

# # print(data)
# # print(data.keys())
# # print(list(data.keys()))

# for key in data.keys():
#     print(key)
#     print(data[key]["connectStatus"])

# data["https://jidae.com"]["connectStatus"] = False
# for key in data.keys():
#     print(key)
#     print(data[key]["connectStatus"])

# # print("=========")
# # print(data["https://jidae.com"])
# # print(data["https://jidae.com"]["connectStatus"])
# # data["https://jidae.com"]["connectStatus"] = False
# # print(data["https://jidae.com"])
# # print(data["https://jidae.com"]["connectStatus"])
# # print(data["https://jidae.com"]["mails"])
# # print(data["https://ruliweb.com"]["mails"][0])
# # print(data["https://ruliweb.com"]["mails"][1])

