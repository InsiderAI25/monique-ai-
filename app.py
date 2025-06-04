from flask import Flask
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Monique Email Service is active."

@app.route("/send")
def send_email():
    msg = EmailMessage()
    msg.set_content("✅ Monique is live and sending this test email.")
    msg['Subject'] = "Test Email from Monique"
    msg['From'] = os.environ.get("EMAIL_USER")
    msg['To'] = os.environ.get("EMAIL_TO")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
    server.send_message(msg)
    server.quit()
    return "Email sent successfully!"
