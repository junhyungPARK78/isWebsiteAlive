# 다른 파일의 함수를 사용하기 : import해서 사용한다.
import schedule
import time
from resources import sendMail
from resources import canConnectWeb

print(canConnectWeb.canConnectWeb(url))
sendMail.sendMail()

saveData = {
    "https://ruliweb.com": {
        "connectStatus": True,
        "mails": ["createzone@gmail.com", "ireieri@me.com"],
    },
    "https://jidae.com": {
        "connectStatus": True,
        "mails": ["createzone@gmail.com"],
    }
}

# https://wikidocs.net/137924

# step1.관련 패키지 및 모듈 import

# step2.실행할 함수 선언
def message():
    print(saveData)
    print(saveData["https://ruliweb.com"])
    print(saveData["https://ruliweb.com"]["connectStatus"])
    print(saveData["https://ruliweb.com"]["mails"])
    print(saveData["https://ruliweb.com"]["mails"][0])
    print(saveData["https://ruliweb.com"]["mails"][1])
    print(saveData["https://jidae.com"]["mails"])
    print(saveData["https://jidae.com"]["mails"][0])

# step3.실행 주기 설정
# schedule.every(60).minutes.do(message)
schedule.every(3).seconds.do(message)

# step4.스캐쥴 시작
while True:
    schedule.run_pending()
    time.sleep(1)

# ======================================================
# 참 거짓을 뒤집는 방법
qwas = False
print(qwas)
print(not qwas)
# ======================================================