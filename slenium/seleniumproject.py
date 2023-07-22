from selenimum import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

a=Service("C:/Users/soura/OneDrive/Desktop/chromedriver_win32/chromedriver.exe")
driver=chrome.webdriver(service=a)
driver.get("https://www.google.com/")
google_search=driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
google_search.send_keys("youtube")
google_search.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath("""/html/body/div[2]/div[2]/div[1]/div[6]/div[3]/div/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/a/div/div[2]/div""").click()
driver.find_element_by_xpath("""/html/body/ytm-app/ytm-mobile-topbar-renderer/header/div/button/c3-icon/svg""").click()
google_search.send_keys("ndtv")
google_search.send_keys(Keys.ENTER)
google_search.save_screenshot("C:/Users/soura/OneDrive/Desktop/slenium/selenium.jpg")