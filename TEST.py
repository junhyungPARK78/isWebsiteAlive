# 다른 파일의 함수를 사용하기 : import해서 사용한다.
from resources import sendMail
from resources import canConnectWeb

url = ""
url = "https://naver.com"
url = "https://jidae.com"
# url = "https://jidaeee.com"
# url = "https://ruliweb.com"
# url = "https://naver.com/1"
# url = "https://jidae.com/1"
# url = "https://jidae.com/2021/03/02/immediatelyBankTransfer/"

# sendMail.sendMail()
print(canConnectWeb.canConnectWeb(url))

# commit test