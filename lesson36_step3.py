from selenium import webdriver
import time
import unittest
import math
import pytest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", 
    "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236905/step/1", 
    "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236903/step/1", 
    "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236898/step/1"])
def test_guest_should_see_correct(browser, link):
    browser.get(link)
    browser.implicitly_wait(10)
    inp = browser.find_element_by_tag_name("textarea")
    inp.send_keys(str(math.log(int(time.time()))))
    but = browser.find_element_by_css_selector("button[class='submit-submission']")
    but.click()
    expected_str = browser.find_element_by_tag_name("pre").text
    assert expected_str == "Correct!", expected_str