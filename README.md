# isWebsiteAlive

**파이썬 버전**
Python 3.9.13

**이전 스크립트 내용**
https://script.google.com/home/projects/1UDGucuwfUK2_jRdh9-6WvyuEte73oM1qOvPFo2YFo5N_8Xbasinxmwh8/edit

**관련 시트**
https://docs.google.com/spreadsheets/d/1x-OR7nX4vt2pyUKpYhQCnB3SSnF2mRybr-z0ayglY6w/edit#gid=0

**pyinstaller 사용법**
https://coding-kindergarten.tistory.com/84
https://taedi.net/11
먼저 spec파일을 만들어두고 : `pyinstaller --onefile --name isWebsiteAlive main.py`
그 후에는 이 명령으로 동일한 스펙의 실행파일을 만들 수 있다. : `pyinstaller isWebsiteAlive.spec`

**VS code에서 가상환경 구축하는 방법**
https://mr-spock.tistory.com/19

**명령어 정리**
- 가상 환경 만들기
  `python3 -m venv 가상 환경의 이름`
- 설치된 패키지 확인
  `pip freeze`
- 설치된 패키지를 관리하는 requirements.txt 파일 만들기
  `pip freeze > requirements.txt`
- requirements.txt 에 적혀있는 패키지 설치하기
  `pip install -r requirements.txt`
- requirements.txt 에 적혀있는 패키지 삭제하기
  `pip uninstall -r requirements.txt -y`
- 가상환경 터미널에서 활성화시키기
  `source pTest_venv/bin/activate`
