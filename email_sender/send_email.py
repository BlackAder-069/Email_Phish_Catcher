import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Test email with suspicious link: http://malicious.example.com")
msg["Subject"] = "Test Phishing Email"
msg["From"] = "attacker@example.com"
msg["To"] = "victim@example.com"

with smtplib.SMTP("localhost", 1025) as server:
    server.send_message(msg)