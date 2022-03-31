from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os 

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Nastya")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Sav")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("myemail.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()