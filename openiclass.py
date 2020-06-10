import sys
import os
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')
browser = webdriver.Chrome()
browser.get('https://sso.tku.edu.tw/NEAI/logineb.jsp?myurl=https://sso.tku.edu.tw/iclass/login?next=/user/index&sso=yes')

def openiclass():
#        python_botton = browser.find_elements_by_xpath('//*[@id="username"]')[0]
        python_button.click()
 

if __name__ == "__main__":
    openiclass()
