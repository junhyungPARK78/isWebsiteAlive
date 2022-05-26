# 파이썬에서 LINE 메세지 보내기
# https://kwonkyo.tistory.com/520

import requests

try:
    TARGET_URL = 'https://notify-api.line.me/api/notify'
    TOKENS = {
        True: 'TsPKQupoFJYa0HrVMmliPHbnyK40f2XrCZcN41lVNWd',
        False: 'AbOPMw01vcCuQcovpbvJQq6X5WKS4wCsxgKduaLuDxr'}
    headers={'Authorization': 'Bearer ' + TOKENS[True]}
    data={'message': f"asdf\n"}

    response = requests.post(TARGET_URL, headers=headers, data=data)

except Exception as ex:
    print(ex)

