from selenium import webdriver
import time
inp = str(raw_input('What you want to search : '))
browser = webdriver.Firefox()
browser.get('http://google.com')
#Inspect element on google.com gives the input class as gsfi
elem = browser.find_element_by_class_name('gsfi')
elem.send_keys(inp)
elem.submit()
time.sleep(6)
elem = browser.find_element_by_class_name('r')
elem.click()