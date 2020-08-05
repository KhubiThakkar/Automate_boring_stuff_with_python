from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
print(type(browser))
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_link_text('Read Online for Free')
    elem.click()
    htmlElem = browser.find_element_by_tag_name('html')
    htmlElem.send_keys(Keys.END)
except:
    print('Was not able to find an element with that name.')