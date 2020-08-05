#!python3
#Emailer.py -- Send an email to the Id and with plain text you input in the command window

#does not work with selenium as gmail doesnot allow automation fireware to loggin your email

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# browser = webdriver.Firefox()
# browser.get('http://www.gmail.com')
# userElem=browser.find_element_by_id('identifierId')
# userElem.send_keys('thakkarmitthi@gmail.com')
# userElem.send_keys(Keys.ENTER)
# passElem = browser.find_element_by_id('password')
# passElem.send_keys('Khubi@123')

import smtplib,ssl
#make sure your security settings are changed for mail Id
sender_email = "thakkarmitthi@gmail.com"
reciever_email = "example@gmail.com"
message = """\
    Subject: Hello ther
     
     
    this message is sent from python"""
port = 465
smtp_server = "smtp.gmail.com"
password = input("enter your password")
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,reciever_email,message)