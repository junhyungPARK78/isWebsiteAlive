# https://wikidocs.net/137924

# step1.관련 패키지 및 모듈 import
import schedule
import time

# step2.실행할 함수 선언
def message():
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print("스케쥴 실행중... : {}", now)

# step3.실행 주기 설정
schedule.every(3).seconds.do(message)

message()

# step4.스캐쥴 시작
while True:
    schedule.run_pending()
    time.sleep(1)
