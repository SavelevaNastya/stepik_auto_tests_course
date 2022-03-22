from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x, y):
  return int(x) + int(y)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    z = str(calc(x, y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)

    option3 = browser.find_element_by_css_selector("button[type='submit']")
    option3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()