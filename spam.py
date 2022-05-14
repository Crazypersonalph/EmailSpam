import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

RECEIVER = os.getenv("RECEIVER")

msg = EmailMessage()

msg['Subject'] = 'Hello'
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECEIVER
msg.set_content('This is a test email')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    while True:
        smtp.send_message(msg)