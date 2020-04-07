import smtplib, datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def sendMail():
    # 发送邮箱服务器
    smtpServer = 'smtp.qq.com'
    smtmport = 465
    # 发送邮箱用户密码
    user = '906201400@qq.com'
    password = 'vksirtaowdadbebg'
    # 发送邮箱
    sender = '906201400@qq.com'
    # 接收邮箱
    receiver = '2602427150@qq.com'
    # 发送邮箱主题
    subject = 'python email test'
    msg = MIMEText('正文内容')
    msg['Subject'] = 'subject qtest'
    msg['From'] = sender
    msg['To'] = receiver

    # 连接发送邮件
    # smtp = smtplib.SMTP(smtpServer, smtmport)
    smtp = smtplib.SMTP_SSL(smtpServer, smtmport)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())

    smtp.quit()

def sendMailAttach(filename):
    # 发送邮箱服务器
    smtpServer = 'smtp.qq.com'
    smtmport = 465
    # 发送邮箱用户密码
    user = '906201400@qq.com'
    password = 'vksirtaowdadbebg'
    # 发送邮箱
    sender = '906201400@qq.com'
    # 接收邮箱
    receiver = '2602427150@qq.com'
    msg = MIMEMultipart()
    att = MIMEText(open(filename, 'rb').read(), 'base64', 'gb2312')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="'+filename[14:]+'"'
    msg.attach(att)

    msg['From'] = sender
    msg['To'] = receiver
    msg['subject'] = Header('Test结果(' + str(datetime.date.today()) + '）', 'gb2312')
    body = 'python test mail'
    msg.attach(MIMEText(body, 'plain'))

    smtp = smtplib.SMTP_SSL(smtpServer, smtmport)
    smtp.login(user, password)
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    sendMailAttach()
