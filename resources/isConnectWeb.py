# https://appia.tistory.com/293

import requests
 
url = ""
url = "https://naver.com"
url = "https://jidae.com"
url = "https://jidaae.com"
url = "https://ruliweb.com"
url = "https://naver.com/1"
url = "https://jidae.com/1"
url = "https://jidae.com/2021/03/02/immediatelyBankTransfer/"

result=requests.get(url)

print("------------------")
print(url)
print(result)
print("------------------")