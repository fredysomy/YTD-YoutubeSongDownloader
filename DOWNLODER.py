from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

a=input("name")

driver = webdriver.Chrome('E:\cfhcghcg\chromedriver.exe')
aa="https://www.youtube.com/results?search_query="+a
driver.get(aa)

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "video-title")))
links = driver.find_elements_by_id("video-title")

a=links[0].get_attribute('href')

driver.get('https://ytmp3.cc/en13/')
driver.find_element_by_id('input').send_keys(a)
driver.find_element_by_id('submit').click()

time.sleep(3)
a=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]')
song=a.get_attribute('href')
driver.get(song)








