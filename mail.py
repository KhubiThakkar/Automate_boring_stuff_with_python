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
    msg['Subject'] = "WIFI not working since 7th September"
    body = "Hey, My registration number is 9625122457 under the name 'Parul Thakkar'. My YOU broadband connection has been inactive since 7th September, 2020. No technician has yet came to check and mend the connection.I have been complaining on the customer care number everyday and there has been no effect. \nI am facing a lot of trouble due to this, as my placements are going on and also I am unable to attend my lectures.\nI am going to spam this mail ID till my connection is fixed.\nYours sincerely,\nFrustrated Customer"

    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "YOUR PASSWORD")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    i+=1
