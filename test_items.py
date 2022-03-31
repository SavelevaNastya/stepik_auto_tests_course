import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button(browser):
    browser.get(link)
    time.sleep(5)
    butt = browser.find_element_by_css_selector("button[type='submit']")
    assert butt != None, "Can't see the button..."