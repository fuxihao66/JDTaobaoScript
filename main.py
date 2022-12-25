from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import datetime

from datetime import date
driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

driver.get("https://www.jd.com")
query = ''' 
login();
'''
driver.execute_script(query)

# element = driver.find_element(By.CLASS_NAME, "link-login")
# print(element)
# driver.get("https://item.jd.com/100035048606.html")

while(1):
    try:
        element = driver.find_element(By.CLASS_NAME, "nickname")
        print('login!!!')
        break
    except NoSuchElementException: 
        print('not logined yet')

time.sleep(1)
driver.get("https://cart.jd.com")
time.sleep(1)

targetHour = 20
targetMinute = 29
targetSecond = 59
 
while(1):
    localTimeTuple = time.localtime()
    hour = localTimeTuple[3]
    minute = localTimeTuple[4]
    second = localTimeTuple[5]
    if hour == targetHour and minute == targetMinute and second == targetSecond:
        try:
            elementList = driver.find_elements(By.CLASS_NAME, "cart-tbody")
            elementList[0].find_elements_by_class_name("jdcheckbox")[0].click()
            time.sleep(0.01)
            submitButton = driver.find_element(By.CLASS_NAME, "common-submit-btn")
            submitButton.click()

            query = ''' 
            submit_Order(null,2);
            '''
            driver.execute_script(query)
        except:
            pass
    else:
        time.sleep(0.1)
# for element in elementList:
#     checkbox = element.find_elements_by_class_name("jdcheckbox")[0]
#     checkbox.click()
#     print("has clicked")

