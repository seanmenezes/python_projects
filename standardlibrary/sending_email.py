from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path
from string import Template

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Sean Menezes"
message["to"]  = "menezessean74@gmail.com"
message["subject"] = "This is a test"
body = template.substitute({"name":"john"})
# you can pass dictionary or keyword argument here
#body = template.substitute(name="John")
message.attach(MIMEText(body,"html"))
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("sean.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("test@gmail.com","test124")
    smtp.send_message(message)
    print("Sent....")