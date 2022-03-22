from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    # Прикол в том, что кнопка появляется не сразу, и без задержек time.sleep(5) тест упадет, не найдя кнопку
    # Но зачастую хз сколько ставить задержку, поэтому используем неявное ожидание browser.implicitly_wait(5)
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/wait1.html"
    browser.get(link)
    #time.sleep(5)
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    button = browser.find_element_by_id("verify").click()
    message = browser.find_element_by_id("verify_message").text

    assert message == "Verification was successful!"
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()