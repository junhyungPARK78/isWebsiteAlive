# 다른 파일의 함수를 사용하기 : import해서 사용한다.
from resources import sendMail
from resources import canConnectWeb

url = ""

# url = "https://jidaeee.com"
# url = "https://ruliweb.com"
# url = "https://naver.com/1"
# url = "https://jidae.com/1"
# url = "https://jidae.com/2021/03/02/immediatelyBankTransfer/"

# sendMail.sendMail()
# print(canConnectWeb.canConnectWeb(url))

url1 = "https://naver.com"
url2 = "https://jidae.com"

mail1 = "zxc@gmail.com"
mail2 = "asd@gmail.com"
mail3 = "qwe@gmail.com"

groupData = {
    url1: [mail1, mail2],
    url2: [mail3]
}

print(groupData)
print(groupData[url2])
# print(groupData["https://jidae.com"])