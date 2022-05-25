# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=xowww&logNo=220987549179
# https://pjw48.net/wordpress/2017/03/22/make-json-py/
# https://pjw48.net/wordpress/2017/03/23/json-parsing-py/

import os
import json

# 세이브 데이터 path 지정
resourcesPath = os.path.abspath("resources")
saveJsonPath = f'{resourcesPath}/saveData.json'

# Reset JSON
def resetSaveData():
    defaultData = {}

    # 세이브 데이터 구조체 Start
    defaultData["https://ruliweb.com"] = {}
    defaultData["https://ruliweb.com"]["connectStatus"] = True
    defaultData["https://ruliweb.com"]["mails"] = ["createzone@gmail.com", "ireieri@me.com"]

    defaultData["https://jidae.com"] = {}
    defaultData["https://jidae.com"]["connectStatus"] = True
    defaultData["https://jidae.com"]["mails"] = ["createzone@gmail.com"]
    # 세이브 데이터 구조체 End

    writeSaveData(defaultData)

# Write JSON
def writeSaveData(saveData):
    with open(saveJsonPath, 'w', encoding="utf-8") as make_file:
        json.dump(saveData, make_file, ensure_ascii=False, indent="\t")

# Open JSON
def openSaveData():
    with open(saveJsonPath, encoding="utf-8") as data_file:    
        savedData = json.load(data_file)

    return savedData

if __name__=="__main__":
    resetSaveData()

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

