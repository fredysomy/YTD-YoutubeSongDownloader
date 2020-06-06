from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from tkinter import*
root=Tk()
root.resizable(0,0)
root.geometry("400x200")
lab=Label(root,text="Youtube Video Downloader")
lab.place(x=120,y=0)
lab1=Label(root,text="Enter name of song").place(x=0,y=50)
entr1=Entry(root)
entr1.place(x=120,y=50)
lab2=Label(root)
lab2.place(x=0,y=130)
driver = webdriver.Chrome('E:\cfhcghcg\chromedriver.exe')
driver.minimize_window()
global a
def initial():
    a=str(entr1.get())
    aa="https://www.youtube.com/results?search_query="+a
    driver.get(aa)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "video-title")))
    links = driver.find_elements_by_id("video-title")
    b=links[0].text
    lab2.configure(text=b+"-Downloaded")
    a=links[0].get_attribute('href')
    time.sleep(3)
    driver.minimize_window()
    driver.get('https://ytmp3.cc/en13/')
    driver.find_element_by_id('input').send_keys(a)
    driver.find_element_by_id('submit').click()
    time.sleep(1)
    ab=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]')
    song=ab.get_attribute('href')
    driver.get(song)
    driver.get('chrome://downloads/')
    driver.maximize_window()

but1=Button(root,text="Download!",width="8",command=initial).place(x=160,y=90)

root.mainloop()
