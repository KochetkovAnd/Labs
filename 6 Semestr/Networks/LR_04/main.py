import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from PyQt5.QtWidgets import *



def createMsg():
    return MIMEMultipart("alternative")

def add(msg):
    workdir = QFileDialog.getOpenFileName()[0]
    with open(workdir, "rb") as f:
        data = f.read()
        attach_part = MIMEBase("application", "octet-stream")
        attach_part.set_payload(data)

    encoders.encode_base64(attach_part)
    attach_part.add_header("Content-Disposition", f"attachment; filename= {workdir}")
    msg.attach(attach_part)


def sendMail(msg, email, password, FROM, TO, messageText, subject, serverAdress, port):    
    msg["Subject"] = subject
    
    text_part = MIMEText(messageText, "plain")
    msg.attach(text_part)

    server = smtplib.SMTP(serverAdress, port)
    server.starttls()
    server.login(email, password)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()




