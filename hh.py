from selenium.webdriver.common.by import By
import time
import pickle
import random
from src.br_src import driver

type_of_work = "vacancy_response"  # vacancy_response, covering_letter
driver.maximize_window()

words_for_search = "qa+automation"
search_url = f"https://hh.ru/search/vacancy?st=searchVacancy&text={words_for_search}&area=113&&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&no_magic=true&L_save_area=true"
pages = range(1, 15)

driver.get('https://hh.ru')

for cookie in pickle.load(open(r'E:\Gurov_SSD_256\IT\Testing\Automation_08_09_2019\hh\src\cookies.pkl', "rb")):
    if 'sameSite' in cookie:
        if cookie['sameSite'] == 'None':
            cookie['sameSite'] = 'Strict'
    driver.add_cookie(cookie)
time.sleep(random.randint(2, 4))
# driver.get(f'{search_url}{words_for_search}')  # '&page=0')
driver.get("https://hh.ru/applicant/negotiations?state=&filter=active&page=0")
# driver.refresh()
time.sleep(random.randint(2, 4))

if type_of_work == "vacancy_response":
    driver.get(f'{search_url}{words_for_search}')  # '&page=0')
    driver.refresh()
    time.sleep(random.randint(2, 4))

    it = 0
    limits = False
    for i in pages:
        if limits:
            break
        driver.get(
            f'{search_url}{words_for_search}&page={str(i)}')
        time.sleep(random.randint(2, 4))
        for i1 in driver.find_elements(By.XPATH, "//*[@data-qa='vacancy-serp__vacancy_response']"):
            time.sleep(random.randint(2, 4))
            try:
                i1.click()
                time.sleep(1)
            except:
                pass

            it += 1
            print(it)

            # if driver.find_element(By.XPATH,
            #                       "//*[@class='Bloko-Notification-Manager notification-manager']").is_displayed():
            #    limits = True
            #    print("STOP")
            #    break

if type_of_work == "covering_letter":

    text_for_hr = '''
Здравствуйте. 
Предлагаю рассмотреть себя в качестве специалиста по автоматизации тестирования.
Немного о себе.
Инженер по тестированию программного обеспечения с опытом работы в области контроля качества, 
со специализацией в автоматизации программного обеспечения и ручном тестировании для веб-интерфейса (UI) и API, 
CI / CD.
Мой стек: Python/PyTest/Allure/Jenkins+Postman/Charles Proxy Server/Fiddler
По необходимости предоставлю пример своего кода.
C уважением, Вик
Телеграм: @lupusludens
'''
    
    for i in pages:
        print(i)
        driver.get("https://hh.ru/applicant/negotiations?state=&filter=active&page=" + str(i))
        time.sleep(random.randint(2, 4))
        for row_v in driver.find_elements(By.XPATH, "//*[@data-qa='negotiations-item-vacancy']"):
            row_v.click()

            time.sleep(random.randint(1, 2))

            driver.switch_to_window(driver.window_handles[1])
            try:
                driver.find_element(By.XPATH, "//*[@data-qa='negotiations-write']").click()
                time.sleep(random.randint(1, 2))
                driver.find_element(By.XPATH, "//*[@data-qa='negotiations-new-message']").send_keys(text_for_hr)
                time.sleep(random.randint(1, 2))
                driver.find_element(By.XPATH, "//*[@data-qa='negotiations-save']").click()
                time.sleep(random.randint(1, 2))
                driver.close()
                driver.switch_to_window(driver.window_handles[0])
            except:
                driver.close()
                driver.switch_to_window(driver.window_handles[0])

driver.quit()
