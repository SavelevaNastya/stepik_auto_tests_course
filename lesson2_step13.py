from selenium import webdriver
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        input1.send_keys("Nastya")
        input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        input2.send_keys("Sav")    
        input4 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        input4.send_keys("my_email")

        button = browser.find_element_by_tag_name("button")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Sorry, your registration failed")
        time.sleep(3)
        browser.quit()
        
        
    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        input1.send_keys("Nastya")
        input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        input2.send_keys("Sav")    
        input4 = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        input4.send_keys("my_email")

        button = browser.find_element_by_tag_name("button")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Sorry, your registration failed")
        time.sleep(3)
        browser.quit()

if __name__ == "__main__":
    unittest.main()

    