# https://docs.python.org/3.9/library/email.examples.html


# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
# with open(textfile) as fp:
#     # Create a text/plain message
#     msg = EmailMessage()
#     msg.set_content(fp.read())

msg = EmailMessage()
msg.set_content('실험실험')

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of ㅁㄴㅇㄹ'
msg['From'] = 'createzonebot@gmail.com'
msg['Bcc'] = 'createzone+TEST@gmail.com, createzone+TEST2@gmail.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls() # TLS 보안 시작
s.login('createzonebot@gmail.com', 'jedzbhlcxotjqyln') # 로그인 인증
s.send_message(msg)
s.quit()