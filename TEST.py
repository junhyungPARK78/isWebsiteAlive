# 다른 파일의 함수를 사용하기 : import해서 사용한다.
import schedule
import time
from resources import sendMail
from resources import canConnectWeb
from resources import withJson

print(canConnectWeb.canConnectWeb("https://ruliweb.com"))
sendMail.sendMail()
# data = withJson.openSaveData()

# # https://wikidocs.net/137924

# # step1.관련 패키지 및 모듈 import

# # step2.실행할 함수 선언
# def message():
#     print(data)
#     print(data["https://ruliweb.com"])
#     print(data["https://ruliweb.com"]["connectStatus"])
#     print(data["https://ruliweb.com"]["mails"])
#     print(data["https://ruliweb.com"]["mails"][0])
#     print(data["https://ruliweb.com"]["mails"][1])
#     print(data["https://jidae.com"]["mails"])
#     print(data["https://jidae.com"]["mails"][0])

# # step3.실행 주기 설정
# # schedule.every(60).minutes.do(message)
# schedule.every(3).seconds.do(message)

# # step4.스캐쥴 시작
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# ======================================================
# 참 거짓을 뒤집는 방법
qwas = False
print(qwas)
print(not qwas)
# ======================================================