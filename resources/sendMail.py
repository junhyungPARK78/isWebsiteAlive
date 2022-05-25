# https://docs.python.org/3.9/library/email.examples.html
# https://yeolco.tistory.com/93

def sendMail():
    import smtplib
    from email.mime.text import MIMEText
    from email.message import EmailMessage
    import time

    # 보낼 메시지 설정
    msg = EmailMessage()
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    msg.set_content(f'내용 : 본문내용 테스트입니다. : {now}')
    msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'
    msg['From'] = 'createzonebot@gmail.com'
    msg['To'] = ''
    msg['Bcc'] = 'createzone+TEST@gmail.com, createzone+TEST2@gmail.com'

    # print(msg.keys())

    # 메일 발송
    mailSession = smtplib.SMTP('smtp.gmail.com', 587) # 세션 생성
    mailSession.starttls() # TLS 보안 시작
    mailSession.login('createzonebot@gmail.com', 'jedzbhlcxotjqyln') # 로그인 인증
    mailSession.send_message(msg)
    mailSession.quit() # 세션 종료

if __name__=="__main__":
    sendMail()