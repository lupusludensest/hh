from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle
import random
from src.br_src import driver

driver.get('https://hh.ru/account/login?backurl=%2F')
#вставить свой емайл и ОБЯЗАТЕЛЬНО ЗАПУСКАТЬ В РЕЖИМЕ ДЕБАГИНГА УСТАНОВИВ ПОИНТЫ НА КАЖДОЙ СТРОЧКЕ 
driver.find_element(By.XPATH, "//input[@name='login']").send_keys("sanoy2006@rambler.ru")

#ЭТУ СТРОЧКУ ЗАПУСКАТЬ КОГДА ПОЛНОСТЬЮ ЗАЛОГИНИШСЯ
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
driver.quit()
