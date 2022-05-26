from resources import withJson
from resources import canConnectWeb
from resources import sendMail

data = withJson.openSaveData()
oldStatus = True
newStatus = True

for keyWebpage in data.keys():
    oldStatus = data[keyWebpage]['connectStatus']
    newStatus = canConnectWeb.canConnectWeb(keyWebpage)

    # 세이브 데이터의 웹페이지 접속가능 여부와 현재 상태의 비교
    if oldStatus == newStatus:
        print((
            # f"======================================================\n"
            f"`{keyWebpage}`\n"
            f"접속 스테이터스가 변하지 않았습니다."
        ))
    else:
        print((
            # f"======================================================\n"
            f"`{keyWebpage}`\n"
            f"접속 스테이터스가 변했습니다."
        ))

        # 메일 내용 생성
        statusName = {True: "접속 가능", False: "접속 불가능"}
        mailContent = (
            # f"======================================================\n"
            f"`{keyWebpage}`\n"
            f"접속 상태가 「{statusName[oldStatus]}」에서 「{statusName[newStatus]}」으로 바뀌었습니다."
        )
        mailSubject = f"{keyWebpage}에 접속 가능 여부에 변경이 있었습니다."
        mailSender = 'createzonebot@gmail.com'
        mailReceiverBcc = ', '.join(s for s in data[keyWebpage]["mails"])

        # 스테이터스 변경을 세이브 데이터에 적용
        data[keyWebpage]['connectStatus'] = newStatus
        withJson.writeSaveData(data)

        # 메일 발송하기
        sendMail.sendMail(mailContent, mailSubject, mailSender, mailReceiverBcc)