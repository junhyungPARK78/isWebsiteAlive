from resources import withJson

aText = 'TESTEST'

testText = f"""
asdf{aText}
qwer
zxcv{aText}{aText}
"""

print(testText)

data = withJson.openSaveData()
print(data['https://ruliweb.com']['shouldSendLineMsg'])
