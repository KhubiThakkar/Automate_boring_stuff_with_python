import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()

valueSearch = sys.argv[1]

browser.get('https://www.flickr.com/photos/tags/photos/')
searchElem = browser.find_element_by_id('search-field')
searchElem.send_keys(valueSearch)
searchElem.send_keys(Keys.ENTER)

