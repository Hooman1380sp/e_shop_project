import smtplib
from email.message import EmailMessage
from django.contrib.auth import get_user_model

User = get_user_model()


# function send mail active account
def SendMail(to, address, random_str):
    EMAIL_HOST_PASSWORD = 'qjvhrbqewwvqxmxp'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'testingmyworksdjango@gmail.com'
    EMAIL_PORT_SSL = 465
    msg = EmailMessage()
    msg['Subject'] = 'Activate account'
    msg['Form'] = EMAIL_HOST_USER
    msg['To'] = to
    msg.set_content(f'{address}{random_str}')
    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(msg)
