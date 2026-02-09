import smtplib
from email.message import EmailMessage
import os

def send_mail(content):
    msg = EmailMessage()
    msg["Subject"] = "US Finance Daily Highlights"
    msg["From"] = os.environ["MAIL_USER"]
    msg["To"] = os.environ["MAIL_USER"]
    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(
            os.environ["MAIL_USER"],
            os.environ["MAIL_PASS"]
        )
        smtp.send_message(msg)

