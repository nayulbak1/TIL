import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD:')

to_email_list = ['edujunho.hphk@gmail.com', 'nayulbak1@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'SSAFY 공지사항'
msg['From'] = 'theskypond@naver.com'
msg['To'] = email
msg.set_content('오늘부터 야자가 필참입니다.')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('theskypond', password)
ssafy.send_message(msg)

print('이메일 전송 완료!')