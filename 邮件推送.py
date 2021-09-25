import smtplib
from email.mime.text import MIMEText
msg_from=''     #发送方邮箱
passwd=''       #填入发送方邮箱的授权码
msg_to=''       #收件人邮箱
smtp=""         #邮件服务器地址
port=""         #邮件服务器端口号(SSL)
                            
subject="python邮件测试"    #主题     
content="测试"                #正文
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL(smtp,port)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print('发送成功')
except smtplib.SMTPException as e:
    print('发送失败',e) #打印错误
finally:
    s.quit()
