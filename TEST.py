# 다른 파일의 함수를 사용하기 : import해서 사용한다.
import schedule
import time
# from resources import sendMail
# from resources import canConnectWeb

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

# https://wikidocs.net/137924

# step1.관련 패키지 및 모듈 import

# step2.실행할 함수 선언
def message():
    print(groupData)
    print(groupData[url2])
    # print(groupData["https://jidae.com"])

# step3.실행 주기 설정
schedule.every(60).minutes.do(message)
# schedule.every(3).seconds.do(message)

# step4.스캐쥴 시작
while True:
    schedule.run_pending()
    time.sleep(1)
