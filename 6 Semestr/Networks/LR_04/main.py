import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendMail(email, password, FROM, TO, messageText, subject):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    
    text_part = MIMEText(messageText, "plain")
    msg.attach(text_part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()




