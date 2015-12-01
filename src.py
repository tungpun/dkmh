# coding=utf-8
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
import winsound
driver = webdriver.Firefox()
url = 'http://dangkyhoc.daotao.vnu.edu.vn/dang-nhap'
url2 = 'http://dangkyhoc.daotao.vnu.edu.vn/dang-ky-mon-hoc-nganh-1/'
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 100000 # Set Duration To 1000 ms == 1 second
while(True):
    driver.get(url)
    try:
        usernameInput = driver.find_element_by_id('LoginName')
        passwordInput = driver.find_element_by_id('Password')
        usernameInput.send_keys('YOUR_USERNAME')
        passwordInput.send_keys('YOUR_PASSWORD')
        driver.find_element_by_class_name("icon-signin").click()
    except:
        continue



    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "icon-signout")))
    except:
         print 'error!!!'
         continue
    driver.get(url2)
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "time-table-1-xxx")))
    except:
         print 'error!!!'
         pass
    try:
        checkBox = driver.find_element_by_xpath(""".//*[@id='divDSDK']/table/tbody/tr[8]/td[1]/input""")
        print 'found!!!!'
        checkBox.send_keys(Keys.SPACE)

        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='registration-container']/div[2]/div/div[3]/button").click()
        time.sleep(5)
        #winsound.Beep(Freq, Dur)
        #WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "time-table-1-xxxs")))
    except:
        pass
